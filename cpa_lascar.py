import bencher
import cpa_bencher
import numpy as np

import lascar

from lascar_common import MyNPYContainer, get_partition_function


def guess_function(
    sensitive_value, guess
):  # the guess function is applied on the partitioned values
    return lascar.hamming(lascar.tools.aes.sbox[sensitive_value ^ guess])


class LascarCPABenchCase(cpa_bencher.CPABenchCase):
    @staticmethod
    def cpa_HW(
        pts,
        traces,
        n_classes,
        n_vars,
    ):
        # init the container
        container = MyNPYContainer(traces, pts)
        cpa_engines = [
            lascar.CpaPartitionedEngine(
                "cpa_{}".format(i),
                get_partition_function(i),
                n_classes,
                guess_function,
                range(n_classes),
            )
            for i in range(n_vars)
        ]

        session = lascar.Session(container, engines=cpa_engines, progressbar=False)
        session.run(batch_size="auto")
        guesses = n_vars * [0]
        for ki, k in enumerate("cpa_{}".format(i) for i in range(n_vars)):
            guesses[ki] = np.argmax(np.max(session.engines[k].finalize(), axis=1))
        return guesses


if __name__ == "__main__":
    bencher.run_benches(LascarCPABenchCase, cpa_bencher.bench_cases)
