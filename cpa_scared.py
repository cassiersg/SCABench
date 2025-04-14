import bencher
import cpa_bencher
import numpy as np

import scared


@scared.attack_selection_function
def first_add_key_sb(plain, guesses):
    res = np.empty((plain.shape[0], len(guesses), plain.shape[1]), dtype="uint8")
    for i, guess in enumerate(guesses):
        res[:, i, :] = scared.aes.base.SBOX[np.bitwise_xor(plain, guess)]
    return res


class ScaredCPABenchCase(cpa_bencher.CPABenchCase):
    @staticmethod
    def cpa_HW(
        pts,
        traces,
        n_classes,
        n_vars,
    ):
        # Create the CPA attack object
        cpa_attack = scared.CPAAttack(
            selection_function=first_add_key_sb,
            model=scared.HammingWeight(),
            discriminant=scared.maxabs,
        )
        # Create the ths
        ths = scared.traces.formats.read_ths_from_ram(samples=traces, plain=pts)
        first_round_container = scared.Container(ths, frame=slice(0, traces.shape[1]))
        cpa_attack.run(first_round_container)
        return np.argmax(cpa_attack.scores, axis=0)


if __name__ == "__main__":
    bencher.run_benches(ScaredCPABenchCase, cpa_bencher.bench_cases)
