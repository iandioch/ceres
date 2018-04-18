#!/bin/bash
cd /home/waterloo/ceres/cards/kattis
git clone --depth 1 https://github.com/iandioch/solutions.git /tmp/solutions
cloc --skip-uniqueness --csv --quiet --3 --out=/tmp/cloc.csv /tmp/solutions/kattis
python3 run.py
rm -rf /tmp/solutions
rm /tmp/cloc.csv
