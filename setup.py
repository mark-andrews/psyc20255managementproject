from setuptools import setup
from os import path

import unittest

here = path.abspath(path.dirname(__file__))

def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('psyc20255management', pattern='test*.py')
    return test_suite

with open(path.join(here, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name = "psyc20255management",
      license = 'GNU Public License 3.0',
      version = "0.0.0",
      description = "Tools for the administration of NTU's psyc20255 module.",
      long_description=long_description,
      author = "Mark Andrews",
      author_email = "mjandrews.net@gmail.com",
      packages=["psyc20255management"],
      test_suite='setup.test_suite',
      scripts = [
        'scripts/psyc20255management_admin.py',
      ],
      install_requires=[
        'beautifulsoup4>=4.6.0',
        'bs4>=0.0.1',
        'configobj>=5.0.6',
        'docopt>=0.6.2',
        'six>=1.11.0',
        'SQLAlchemy>=1.1.15'
        ],
)
