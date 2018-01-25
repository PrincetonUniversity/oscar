#!/bin/bash
module load anaconda
conda remove --name test_env --all
conda env create --file ci/requirements.yml
source activate test_env
pip install -e .
