#!/bin/bash
git clone https://github.com/iandioch/solutions.git
cloc --skip-uniqueness --csv --quiet --3 --out=cloc.csv solutions
python3 analyse.py
rm -rf solutions
rm cloc.csv
