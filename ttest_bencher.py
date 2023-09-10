
import numpy as np

import bencher

class TtestBenchCase:
    def __init__(self, n_samples, n_traces, order):
        self.traces = np.random.randint(0,1024,(n_traces,n_samples),dtype=np.int16)
        self.values = np.random.randint(0,2,(n_traces,),dtype=np.uint16)
        self.n_samples = n_samples
        self.n_traces = n_traces
        self.order = order

    def run(self):
        return self.ttest(
                self.traces,
                self.values,
                self.n_samples,
                self.n_traces,
                self.order,
                )

    @staticmethod
    def bench_name(n_samples, n_traces, order):
        return f"ttest_ns={n_samples}_nt={n_traces}_o={order}"


bench_cases = [
        {
            "n_samples": 10**3,
            "n_traces": 5*10**5,
            "order": 1,
            },
        {
            "n_samples": 10**4,
            "n_traces": 10**6,
            "order": 1,
            },
        ]

