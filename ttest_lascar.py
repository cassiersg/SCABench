
import lascar

import bencher
import ttest_bencher

class MyNPYContainer(lascar.Container):
    def __init__(self, traces, data_dic, **kwargs):
        self.leakages = traces
        self.values = data_dic
        lascar.Container.__init__(self, **kwargs)

    def __getitem__(self, key):
        return lascar.TraceBatchContainer.__getitem__(self, key)

    def __setitem__(self, key, value):
        lascar.TraceBatchContainer.__setitem__(self, key, value)

def partition_function(value):
    return value

# benchmarking functions
class LascarTtestBencCase(ttest_bencher.TtestBenchCase):
    @staticmethod
    def ttest(
            traces,
            values,
            n_samples,
            n_traces,
            order,
            ):

        #init the container
        container = MyNPYContainer(traces, values)

        ttest_engine = lascar.TTestEngine("ttest", partition_function, analysis_order=order)

        session = lascar.Session(
            container,
            progressbar=False
        )
        session.add_engine(ttest_engine)

        session.run(batch_size="auto")

if __name__ == '__main__':
    bencher.run_benches(LascarTtestBencCase, ttest_bencher.bench_cases)
