#!/bin/bash
module load anaconda
conda env create --file ci/requirements.yml
source activate test_env
pip install -e .
pytest -vv oscar
