#!/usr/bin/env bash
# exit on error
set -o errexit

conda update --all --yes
conda config --add channels conda-forge
conda install --file requirements.txt --yes

