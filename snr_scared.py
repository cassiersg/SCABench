
import scared

import bencher
import snr_bencher

def id_sf(i):
    return scared.reverse_selection_function(lambda cls: cls[:,i])

# benchmarking functions
class ScaredSNRBencCase(snr_bencher.SNRBenchCase):
    @staticmethod
    def snr(
            traces,
            values,
            n_classes,
            n_samples,
            n_vars,
            n_traces,
            ):
        ths = scared.traces.formats.read_ths_from_ram(samples=traces, cls=values)
        container = scared.Container(ths)

        for i in range(n_vars):
            analysis = scared.SNRReverse(
                selection_function=id_sf(i),
                model=scared.Value()
            )
            analysis.run(container)
        return analysis.results

if __name__ == '__main__':
    bencher.run_benches(ScaredSNRBencCase, snr_bencher.bench_cases)
