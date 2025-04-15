# SCABench

A suite of benchmarks for side-channel analysis libraries.

## Contents

Libraries:

- [lascar](https://github.com/Ledger-Donjon/lascar)
- [SCALib](https://github.com/simple-crypto/SCALib)
- [scared](https://gitlab.com/eshard/scared)


Benchmark cases:

- SNR computation
- First-order T-test computation

Contributions welcome !


## Usage

```
git clone https://github.com/cassiersg/SCABench
cd SCABench
make
```

## Results

**Cautionnary remark:**
It is recommended to adjust the test cases dimensions to your use cases, and
run the benchmarks on your workstation.
We tried to make this benchmark as fair as possible, but performance may widely
depends on configuration and settings.
Also, our current set of benchmarks only covers a small part of the libraries.

Here are some results on a `Intel(R) Xeon(R) CPU E5-2670 v3 @ 2.30GHz` (210 GiB RAM):

| Benchmark |  lascar | SCALib | scared |
| --------- | ------- | ------ | ------ |
| SNR (16 8-bit variables, 1k points per trace, 100k traces) | 24.8s | 0.36s | 43.0s |
| SNR (1 4-bit variable, 10k points per trace, 1M traces) | 36.7s | 1.3s | 21.1s |
| T-test (1st order, 1k points per trace, 500k traces) | 3.1s | 0.51s | 2.7s |
| T-test (1st order, 10k points per trace, 1M traces) | 48.7s | 1.2s | 23.4s |
| CPA (1k points per trace, 1M traces, 16 vars, 256 classes) | 21.3s | 0.178s | 54.6s |
| CPA (10k points per trace, 1M traces, 1 vars, 16 classes) | 14.5s | 1.15s | 38.6s |

## Contribution

We welcome contributions to add more test cases or libraries to the benchmark.

If you find a test case to be missing or the configuration used for a library
to be suboptimal, please open a pull request!

## License

SCABench is released under the MIT License.
