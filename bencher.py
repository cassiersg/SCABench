
import pyperf

def run_benches(bench_case_class, bench_cases):
    runner = pyperf.Runner()
    for bench_case in bench_cases:
        runner.timeit(
                name=bench_case_class.bench_name(**bench_case),
                stmt="bench_runner.run()",
                setup=f"bench_runner= BenchCase(**bench_case)",
                globals={'BenchCase': bench_case_class, 'bench_case': bench_case}
              )

