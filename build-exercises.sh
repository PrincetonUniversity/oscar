#!/bin/bash
module load anaconda
source activate test_env
pytest -vv ../oscar-exercises
