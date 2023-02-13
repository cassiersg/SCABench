
import scared

import bencher
import ttest_bencher

class ScaredTtestBenchCase(ttest_bencher.TtestBenchCase):
    @staticmethod
    def ttest(
            traces,
            values,
            n_samples,
            n_traces,
            order,
            ):
        assert order == 1

        traces0 = values == 0
        traces1 = values == 1
        ths0 = scared.traces.formats.read_ths_from_ram(samples=traces[traces0,:], plaintext=values[traces0])
        ths1 = scared.traces.formats.read_ths_from_ram(samples=traces[traces1,:], plaintext=values[traces1])

        cont = scared.TTestContainer(ths0, ths1)
        analysis = scared.TTestAnalysis(precision='float64')
        analysis.run(cont)

        assert analysis.result is not None


if __name__ == '__main__':
    bencher.run_benches(ScaredTtestBenchCase, ttest_bencher.bench_cases)
