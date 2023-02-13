
import lascar

import bencher
import snr_bencher

class MyNPYContainer(lascar.Container):
    def __init__(self, traces, data_dic, **kwargs):
        self.leakages = traces
        self.values = data_dic
        lascar.Container.__init__(self, **kwargs)

    def __getitem__(self, key):
        return lascar.TraceBatchContainer.__getitem__(self, key)

    def __setitem__(self, key, value):
        lascar.TraceBatchContainer.__setitem__(self, key, value)

def get_partition_function(byte):
    def partition_function(value):
        return value[byte]
    return partition_function

# benchmarking functions
class LascarSNRBencCase(snr_bencher.SNRBenchCase):
    @staticmethod
    def snr(
            traces,
            values,
            n_classes,
            n_samples,
            n_vars,
            n_traces,
            ):

        #init the container
        container = MyNPYContainer(traces, values)

        snr_engines = [
                lascar.SnrEngine("snr_%d" % i, get_partition_function(i), range(n_classes))
                for i in range(n_vars)
                ]

        session = lascar.Session(
            container,
            engines=snr_engines,
            progressbar=False
        )

        session.run(batch_size="auto")

if __name__ == '__main__':
    bencher.run_benches(LascarSNRBencCase, snr_bencher.bench_cases)
