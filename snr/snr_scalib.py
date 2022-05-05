
from scalib.metrics import SNR

import snr_bencher

def snr(
        traces,
        values,
        n_classes,
        n_samples,
        n_vars,
        n_traces,
        threads
        ):

    snr = SNR(nc=n_classes,ns=n_samples,np=n_vars)

    snr.fit_u(traces,values)
    v = snr.get_snr()

    return v

if __name__ == '__main__':
    snr_bencher.run_snr_benches(snr)
