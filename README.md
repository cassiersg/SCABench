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

Here are some results on a `Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz` laptop:

| Benchmark |  lascar | SCALib | scared |
| --------- | ------- | ------ | ------ |
| SNR (16 8-bit variables, 1k points per trace, 1M traces) | 26.8s | 1.1s | n.a. |
| T-test (1st order, 1k points per trace, 500k traces) | 11.4s | 0.26s | 4.7s |

## Contribution

We welcome contributions to add more test cases or libraries to the benchmark.

If you find a test case to be missing or the configuration used for a library
to be suboptimal, please open a pull request!

## License

SCABench is released under the MIT License.
