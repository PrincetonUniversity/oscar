from setuptools import setup, find_packages

setup(name='OSCAR',
      packages=find_packages(),
      install_requires=[
          'scipy',
          'matplotlib',
          ],
      )