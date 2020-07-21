from setuptools import setup, find_packages

setup(name='OSCAR',
      packages=find_packages(),
      install_requires=[
          'scipy==1.4.1',
          'matplotlib==3.2.1',
          'xarray==0.15.1',
          'pandas==1.0.4',
          'numpy==1.18.1'], # matching package versions from py37_OSCAR_windows
      )