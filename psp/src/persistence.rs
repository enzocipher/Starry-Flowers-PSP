//! Persistence bounds and retry timing, independent of PSP system calls.
#[derive(Default)]
pub struct SaveRetry {
    last_attempt: Option<f64>,
}

impl SaveRetry {
    pub fn due(&mut self, now: f64, leaving_game: bool) -> bool {
        let due = match self.last_attempt {
            None => true,
            Some(last) => leaving_game || now - last >= 2.0,
        };
        if due {
            self.last_attempt = Some(now);
        }
        due
    }
}

pub fn valid_indices(indices: &[usize; 3], counts: [usize; 3]) -> bool {
    indices[0] < counts[0] && indices[1] < counts[1] && indices[2] < counts[2]
}

pub fn normalize_indices(indices: &mut [usize; 3], counts: [usize; 3]) {
    for i in 0..3 {
        if indices[i] >= counts[i] {
            indices[i] = 0;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn retry_timing_records_attempts_even_when_io_fails() {
        let mut retry = SaveRetry::default();
        assert!(retry.due(0.0, false));
        assert!(!retry.due(0.016, false));
        assert!(!retry.due(1.99, false));
        assert!(retry.due(2.0, false));
    }

    #[test]
    fn leaving_game_allows_one_immediate_attempt() {
        let mut retry = SaveRetry::default();
        assert!(retry.due(10.0, false));
        assert!(retry.due(10.016, true));
        assert!(!retry.due(10.032, false));
    }

    #[test]
    fn indices_validate_and_normalize_boundaries() {
        let counts = [2, 3, 1];
        assert!(valid_indices(&[0, 0, 0], counts));
        assert!(valid_indices(&[1, 2, 0], counts));
        assert!(!valid_indices(&[2, 0, 0], counts));
        assert!(!valid_indices(&[0, 3, 0], counts));
        assert!(!valid_indices(&[0, 0, 1], counts));
        assert!(!valid_indices(&[usize::MAX; 3], counts));
        let mut indices = [1, usize::MAX, 1];
        normalize_indices(&mut indices, counts);
        assert_eq!(indices, [1, 0, 0]);
        let mut indices = [2, 3, 1];
        normalize_indices(&mut indices, counts);
        assert_eq!(indices, [0, 0, 0]);
        let mut indices = [0, 2, 0];
        normalize_indices(&mut indices, counts);
        assert_eq!(indices, [0, 2, 0]);
    }
}
