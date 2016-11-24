#!/bin/bash
cd /home/waterloo/ceres/cards/euler
git clone https://github.com/iandioch/solutions.git /tmp/solutions
cloc --skip-uniqueness --csv --quiet --3 --out=/tmp/cloc.csv /tmp/solutions/project_euler
python2 analyse.py
rm -rf /tmp/solutions
rm /tmp/cloc.csv
