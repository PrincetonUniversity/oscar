import setuptools


LONG_DESCRIPTION = """
**OSCAR**: a compact Earth system model

Adapted for ENV367 at Princeton University.

Gasser, T., P. Ciais, O. Boucher, Y. Quilcaille, M. Tortora, L. Bopp & D.
Hauglustaine. "The compact Earth system model OSCAR v2.2: description and first
results." Geoscientific Model Development 10: 271-319 (2017).
doi:10.5194/gmd-10-271-2017

Links
-----
 - https://github.com/tgasser/OSCAR
"""


setuptools.setup(
    name='oscar',
    version='0.1',
    packages=setuptools.find_packages(),
    author='T. Gasser et al.',
    description='A compact Earth system model',
    long_description=LONG_DESCRIPTION,
    install_requires=[
        'matplotlib >= 1.5',
        'numpy >= 1.7',
        'scipy >= 0.16'
    ],
    package_data={'oscar': ['data/**']},
    scripts=['oscar/examples/Examples.ipynb']
)
