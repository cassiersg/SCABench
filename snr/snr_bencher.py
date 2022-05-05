
import numpy as np
import pyperf

class SNRBenchCase:
    def __init__(self, n_classes, n_samples, n_vars, n_traces, n_threads):
        self.traces = np.random.randint(0,1024,(n_traces,n_samples),dtype=np.int16)
        self.values = np.random.randint(0,n_classes,(n_traces,n_vars),dtype=np.uint16)
        self.n_classes = n_classes
        self.n_samples = n_samples
        self.n_vars = n_vars
        self.n_traces = n_traces
        self.n_threads = n_threads

    def run_snr(self, snr):
        return snr(
                self.traces,
                self.values,
                self.n_classes,
                self.n_samples,
                self.n_vars,
                self.n_traces,
                self.n_threads,
                )

def bench_name(n_classes, n_samples, n_vars, n_traces, n_threads):
    return f"ns={n_samples}_nc={n_classes}_np={n_vars}_nt={n_traces}"


bench_cases = [
        {
            "n_classes": 256,
            "n_samples": 1000,
            "n_vars": 16,
            "n_traces": 10**4,
            "n_threads": 1,
            },
        {
            "n_classes": 256,
            "n_samples": 1000,
            "n_vars": 16,
            "n_traces": 10**5,
            "n_threads": 1,
            },
        ]

def run_snr_benches(snr):
    runner = pyperf.Runner()
    for bench_case in bench_cases:
        runner.timeit(
                name=bench_name(**bench_case),
                stmt="bench_case.run_snr(snr)",
                setup=f"bench_case = SNRBenchCase(**{bench_case})",
                globals={'SNRBenchCase': SNRBenchCase, 'snr': snr}
              )
