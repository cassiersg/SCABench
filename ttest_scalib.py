
from scalib.metrics import Ttest

import bencher
import ttest_bencher

class ScalibTtestBenchCase(ttest_bencher.TtestBenchCase):
    @staticmethod
    def ttest(
            traces,
            values,
            n_samples,
            n_traces,
            order,
            ):

        ttest = Ttest(ns=n_samples,d=order)

        ttest.fit_u(traces,values)
        v = ttest.get_ttest()

        return v

if __name__ == '__main__':
    bencher.run_benches(ScalibTtestBenchCase, ttest_bencher.bench_cases)
