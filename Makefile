
SHELL := /bin/bash

all: report

ve/%: requirements_%.txt
	mkdir -p ve
	test -d ve/$* || python3 -m venv ve/$*
	( source ve/$*/bin/activate && pip install -U setuptools pip wheel pyperf)
	( source  ve/$*/bin/activate && pip install -r requirements_$*.txt )

results/snr_%.json: snr_%.py snr_bencher.py ve/%
	mkdir -p results
	rm -f $@
	( source ve/$*/bin/activate && python $< -o $@ -w 1 -p 1 -v )

results/ttest_%.json: ttest_%.py snr_bencher.py ve/%
	mkdir -p results
	rm -f $@
	( source ve/$*/bin/activate && python $< -o $@ -n 5 -w 1 -p 1 -v )

results/cpa_%.json: cpa_%.py cpa_bencher.py ve/%
	mkdir -p results
	rm -f $@
	( source ve/$*/bin/activate && python $< -o $@ -n 5 -w 1 -p 1 -v )


SNR_RESULTS = $(addprefix results/snr_,scalib.json lascar.json scared.json)
TTEST_RESULTS = $(addprefix results/ttest_,scalib.json lascar.json scared.json)
CPA_RESULTS = $(addprefix results/cpa_,scalib.json lascar.json scared.json)

report: ve/cmp $(CPA_RESULTS) #$(SNR_RESULTS) $(TTEST_RESULTS)
	( source ve/cmp/bin/activate && pyperf compare_to $(SNR_RESULTS))
	( source ve/cmp/bin/activate && pyperf compare_to $(TTEST_RESULTS))
	( source ve/cmp/bin/activate && pyperf compare_to $(CPA_RESULTS))

clean:
	rm -rf ve
	rm -rf results

.PHONY: clean
