import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="mf_ds_cookiecutter",
    packages=find_packages(),
    version="0.1.0",
    author="Mark Friel",
    keywords="cookiecutter datascience luigi",
    description="A datascience project template incorporating luigi for workflow orchestration.",
    long_description=read("README"),
    license="MIT",
)
