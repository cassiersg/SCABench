import lascar

import bencher
import snr_bencher

from lascar_common import MyNPYContainer, get_partition_function


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

        # init the container
        container = MyNPYContainer(traces, values)

        snr_engines = [
            lascar.SnrEngine("snr_%d" % i, get_partition_function(i), range(n_classes))
            for i in range(n_vars)
        ]

        session = lascar.Session(container, engines=snr_engines, progressbar=False)

        session.run(batch_size="auto")


if __name__ == "__main__":
    bencher.run_benches(LascarSNRBencCase, snr_bencher.bench_cases)
