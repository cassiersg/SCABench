
import numpy as np

class SNRBenchCase:
    def __init__(self, n_classes, n_samples, n_vars, n_traces):
        self.traces = np.random.randint(0,1024,(n_traces,n_samples),dtype=np.int16)
        self.values = np.random.randint(0,n_classes,(n_traces,n_vars),dtype=np.uint16)
        self.n_classes = n_classes
        self.n_samples = n_samples
        self.n_vars = n_vars
        self.n_traces = n_traces

    def run(self):
        return self.snr(
                self.traces,
                self.values,
                self.n_classes,
                self.n_samples,
                self.n_vars,
                self.n_traces,
                )

    @staticmethod
    def bench_name(n_classes, n_samples, n_vars, n_traces):
        return f"snr_ns={n_samples}_nc={n_classes}_np={n_vars}_nt={n_traces}"


bench_cases = [
        {
            "n_classes": 256,
            "n_samples": 1000,
            "n_vars": 16,
            "n_traces": 10**6,
            },
        ]

