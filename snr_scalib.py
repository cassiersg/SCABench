
from scalib.metrics import SNR

import bencher
import snr_bencher

class ScalibSNRBenchCase(snr_bencher.SNRBenchCase):
    @staticmethod
    def snr(
            traces,
            values,
            n_classes,
            n_samples,
            n_vars,
            n_traces,
            ):

        snr = SNR(nc=n_classes,ns=n_samples,np=n_vars)

        snr.fit_u(traces,values)
        v = snr.get_snr()

        return v

if __name__ == '__main__':
    bencher.run_benches(ScalibSNRBenchCase, snr_bencher.bench_cases)
