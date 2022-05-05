
SHELL := /bin/bash

all: snr_scalib.json snr_lascar.json

ve_%: requirements_%.txt
	test -d ve_$* || python3 -m venv ve_$*
	( source ve_$*/bin/activate && pip install -U setuptools pip wheel )
	( source  ve_$*/bin/activate && pip install -r requirements_$*.txt )

snr_%.json: snr_%.py snr_bencher.py ve_%
	( source ve_$*/bin/activate && python $< -o $@ -n 1 -w 1 -p 1 -v )

clean:
	rm -r ve_*
	rm snr_*.json

.PHONY: clean
