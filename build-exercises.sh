#!/bin/bash
module load anaconda
source activate test_env
git clone git@github.com:PrincetonUniversity/oscar-exercises.git
pytest -vv oscar-exercises
