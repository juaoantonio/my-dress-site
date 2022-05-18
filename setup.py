"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
        name="django_my_dress_site", 
        version="1.0", 
        packages=find_packages(), 
        scripts=["manage.py"],
        install_requires = ["django", "pytz", "pillow"]
    )
