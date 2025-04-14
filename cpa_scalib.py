from scalib.attacks import Cpa

import bencher
import cpa_bencher
import numpy as np

import utils_bench_cpa as ub


class ScalibCPABenchCase(cpa_bencher.CPABenchCase):
    @staticmethod
    def cpa_HW(
        pts,
        traces,
        n_classes,
        n_vars,
    ):
        # Generate the useful models array
        hw_models = np.zeros([n_vars, n_classes, traces.shape[1]], dtype=np.float64)
        for c in range(n_classes):
            hw_models[:, c, :] = ub.HW[ub.Sbox[c]].astype(np.float64)
        cpa = Cpa(n_classes, Cpa.Xor)
        cpa.fit_u(traces, pts)
        corr = np.abs(cpa.get_correlation(hw_models))
        return np.argmax(np.max(corr, axis=2), axis=1)


if __name__ == "__main__":
    bencher.run_benches(ScalibCPABenchCase, cpa_bencher.bench_cases)
