import numpy as np


class CPABenchCase:
    def __init__(self, seed, n_classes, n_samples, n_vars, n_traces):
        rng = np.random.default_rng(seed=seed)
        self.pts = rng.integers(0, n_classes, (n_traces, n_vars), dtype=np.uint16)
        self.traces = rng.integers(0, 1024, (n_traces, n_samples), dtype=np.int16)
        self.n_classes = n_classes
        self.n_samples = n_samples
        self.n_vars = n_vars
        self.n_traces = n_traces

    def run(self):
        return self.cpa_HW(
            self.pts,
            self.traces,
            self.n_classes,
            self.n_vars,
        )

    @staticmethod
    def bench_name(seed, n_classes, n_samples, n_vars, n_traces):
        return (
            f"cpa_seed={seed}_ns={n_samples}_nc={n_classes}_np={n_vars}_nt={n_traces}"
        )


bench_cases = [
    {
        "seed": 0,
        "n_classes": 256,
        "n_samples": 1000,
        "n_vars": 16,
        "n_traces": 10**6,
    },
    {
        "seed": 0,
        "n_classes": 16,
        "n_samples": 10000,
        "n_vars": 1,
        "n_traces": 10**6,
    },
]
