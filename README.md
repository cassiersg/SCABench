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

Here are some results on a `AMD Ryzen Threadripper 3990X 64-Core Processor` (256 GiB RAM), Ubuntu 24.04:

| Benchmark |  lascar | SCALib | scared |
| --------- | ------- | ------ | ------ |
| SNR (16 8-bit variables, 1k points per trace, 100k traces) | 17.4s | 0.15s | 17.9s |
| SNR (1 4-bit variable, 10k points per trace, 1M traces) | 14.9s | 1.2s | 7.3s |
| T-test (1st order, 1k points per trace, 500k traces) | 2.2s | 0.02s | 1.0s |
| T-test (1st order, 10k points per trace, 1M traces) | 33.1s | 0.61s | 5.7s |
| CPA (16 8-bit variables, 1k points per trace, 1M traces) | 21.0s | 0.19s | 53.2s |
| CPA (1 4-bit variable, 10k points per trace, 1M traces) | 24.9s | 1.17s | 36.1s |

## Contribution

We welcome contributions to add more test cases or libraries to the benchmark.

If you find a test case to be missing or the configuration used for a library
to be suboptimal, please open a pull request or contact me.

## License

SCABench is released under the MIT License.
