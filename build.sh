#!/bin/bash
module load anaconda
conda env create --file ci/requirements.yml
pip install e .
pytest -vv oscar
conda remove --name test_env --all
