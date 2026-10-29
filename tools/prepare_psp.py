"""Keep source-resolution art in compact GE DXT5 tiles and PSP logical geometry."""
import hashlib, json, math, pathlib, subprocess, shutil
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg
from psp_textures import encode_texture
from psp_pipeline import atomic_json, atomic_write, cached_image_descriptor, cleanup_obsolete, convert_audio_cached, load_valid_manifest, sha256_file, unique_audio_stems, validate_manifest
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'psp/dist/DATA'; OUT.mkdir(parents=True,exist_ok=True)
previous=load_valid_manifest(OUT)
story=json.loads((ROOT/'story.json').read_text(encoding='utf-8'))
story['translations']={k:v for k,v in story['translations'].items() if k=='es'}
(ROOT/'psp/story.json').write_text(json.dumps(story,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
images=dict(story['images']); images.update({'ui '+n:'gui/'+n+'.png' for n in ['main_menu','game_menu','textbox','nvl']})
manifest={'images':{},'fonts':{},'audio':{},'version':9,'art_scale':1.0,'texture_format':'PSP DXT5 / RGBA quality fallback','inline_symbols':story.get('inline_symbols',{})}
files={}; active={'MANIFEST.JSON'}; image_hashes={}; image_cache_hits=0
IMAGE_RECIPE='source-resolution-dxt5-rgba-tiles-248-gutter4-mips-2-v11'
for source,target in [('Twemoji-LICENSE.txt','TWEMOJI.TXT'),('DejaVu-LICENSE.txt','DEJAVU.TXT')]:
 shutil.copyfile(ROOT/'assets/gui/emoji'/source,OUT/target);active.add(target)
shutil.copyfile(ROOT/"licenses/RENPY-LICENSE.txt",OUT/"RENPY.TXT");active.add("RENPY.TXT")
def power2(n): return max(16,1<<(n-1).bit_length())
for name,path in images.items():
 if path not in files:
  source_path=ROOT/'assets'/path
  if path not in image_hashes:image_hashes[path]=sha256_file(source_path)
  source_hash=image_hashes[path]
  cached=cached_image_descriptor(previous,name,source_hash,IMAGE_RECIPE,OUT)
  if cached:
   files[path]=cached; image_cache_hits+=1
   active.update(tile['file'] for tile in cached['tiles'])
   manifest['images'][name]=cached
   continue
  original=Image.open(source_path).convert('RGBA'); ow,oh=original.size
  rw,rh=max(4,((ow+3)//4)*4),max(4,((oh+3)//4)*4); original=original.resize((rw,rh),Image.Resampling.LANCZOS)
  bounds=original.getbbox() or (0,0,1,1)
  bounds=(bounds[0]//4*4,bounds[1]//4*4,min(rw,(bounds[2]+3)//4*4),min(rh,(bounds[3]+3)//4*4))
  levels=[original]+[original.resize((max(1,(rw+(1<<l)-1)//(1<<l)),max(1,(rh+(1<<l)-1)//(1<<l))),Image.Resampling.LANCZOS) for l in [1,2]]
  tiles=[]
  # 248 + gutters fits 256: substantially less power-of-two padding than 448/512.
  for y in range(bounds[1],bounds[3],248):
   for x in range(bounds[0],bounds[2],248):
    w,h=min(248,bounds[2]-x),min(248,bounds[3]-y); tw,th=power2(w+8),power2(h+8)
    filename='T'+hashlib.sha256((path+'@'+source_hash+'@'+IMAGE_RECIPE).encode()).hexdigest()[:12].upper()+f'{x//248:02X}{y//248:02X}.TEX'
    tile_levels=[]
    for level,img in enumerate(levels):
     scale=1<<level
     tile=img.crop(((x-4)//scale,(y-4)//scale,(x-4+tw)//scale,(y-4+th)//scale))
     inset=4//scale
     tile_levels.append((tile,(inset,inset,inset+w//scale,inset+h//scale)))
    data,dxt5=encode_texture(tile_levels)
    atomic_write(OUT/filename,bytes(data)); active.add(filename)
    tiles.append({'file':filename,'x':x,'y':y,'width':w,'height':h,'texture_width':tw,'texture_height':th,'dxt5':dxt5})
  files[path]={'width':max(1,round(ow*.375)),'height':max(1,round(oh*.375)),'original_width':ow,'original_height':oh,'raster_width':rw,'raster_height':rh,'tiles':tiles,'_cache':{'source_sha256':source_hash,'recipe':IMAGE_RECIPE}}
 manifest['images'][name]=files[path]
chars=set(''.join(op.get('text','') for op in story['ops']))
chars.update(''.join(c['heading']+c['body'] for c in story.get('credits',[]))); chars.add('∞'); chars.update(''.join(story['translations'].get('es',{}).values())); chars.update(chr(i) for i in range(32,256))
chars=sorted(c for c in chars if c.isprintable())
for size in [8,10,12,14,18,24]:
 scale=4; font=ImageFont.truetype(str(ROOT/'assets/tl/None/Nunito-Bold.ttf'),size*scale)
 pages=[Image.new('L',(512,512))]; page=0; x=y=2; row=0; glyphs={}
 for c in chars:
  box=font.getbbox(c); w=max(1,box[2]-box[0]); h=max(1,box[3]-box[1]); glyph=Image.new('L',(w,h)); ImageDraw.Draw(glyph).text((-box[0],-box[1]),c,font=font,fill=255)
  left=box[0]/scale; top=box[1]/scale; advance=font.getlength(c)/scale
  if x+w+2>512: x=2;y+=row+4;row=0
  if y+h+2>512: pages.append(Image.new('L',(512,512)));page+=1;x=y=2;row=0
  pages[page].paste(glyph,(x,y)); filename=f'F{size:02}P{page:02}.RAW'
  glyphs[c]={'file':filename,'x':x,'y':y,'width':w,'height':h,'left':left,'top':top,'advance':advance}
  x+=w+4;row=max(row,h)
 for index,image in enumerate(pages):
  filename=f'F{size:02}P{index:02}.RAW'; atomic_write(OUT/filename,image.tobytes());active.add(filename)
 manifest['fonts'][str(size)]={'scale':scale,'ascent':font.getmetrics()[0]/scale,'glyphs':glyphs}
ffmpeg=imageio_ffmpeg.get_ffmpeg_exe()
audio_paths=unique_audio_stems(p for p in (ROOT/'assets/audio').iterdir() if p.suffix.lower() in {'.ogg','.wav'})
manifest['audio_cache']={}; audio_cache_hits=0
for path in audio_paths:
 source_hash=sha256_file(path)
 filename='S'+hashlib.sha256((path.stem.casefold()+'|'+source_hash+'|ffmpeg:s16le:stereo:44100:v1').encode()).hexdigest()[:12].upper()+'.PCM'; dest=OUT/filename
 record,hit=convert_audio_cached(path,dest,source_hash,(previous or {}).get('audio_cache',{}).get(path.stem),ffmpeg)
 manifest['audio_cache'][path.stem]=record; audio_cache_hits+=int(hit)
 manifest['audio'][path.stem]=filename;active.add(filename)
manifest['files']=sorted(active)
validate_manifest(manifest,OUT)
atomic_json(OUT/'MANIFEST.JSON',manifest)
removed=cleanup_obsolete(previous,manifest,OUT)
print(f"Source-resolution DXT5 art: {len(files)} images ({image_cache_hits} cache hits); {sum(len(i['tiles']) for i in files.values())} GPU tiles; audio {audio_cache_hits}/{len(audio_paths)} cache hits; {sum((OUT/p).stat().st_size for p in active)/1024**2:.1f} MiB; removed {len(removed)} obsolete generated files")
