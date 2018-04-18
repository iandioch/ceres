#!/bin/bash
EULERFOILERLOC="/home/waterloo/prog/euler-foiler"
cd /home/waterloo/ceres/cards/euler
git clone --depth 1 https://github.com/iandioch/solutions.git /tmp/solutions
cloc --skip-uniqueness --csv --quiet --progress-rate=0 --3 --out=/tmp/cloc.csv /tmp/solutions/project_euler

cd $EULERFOILERLOC
python3 parse.py -u iandioch >> num_solved.txt
cd -
mv $EULERFOILERLOC/num_solved.txt .
python2 analyse.py
rm -rf /tmp/solutions
rm /tmp/cloc.csv
rm num_solved.txt
