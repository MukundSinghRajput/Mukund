import os, re
from setuptools import find_packages, setup


def read(file_name, version=False):
    text = open(os.path.join(os.path.dirname(__file__), file_name), encoding="utf8").read()
    return text

setup(
    name="Mukund",
    version='1.0.1',
    maintainer='Mukund',
    description="An advance package to store data in JSON files and allow to store media with mapping and much more i recommend to atleast use it once",
    packages=['Mukund', 'Mukund.core', 'Mukund.errors'],
    keywords=["Database", "MukundDrive", "MukundDB", "Mukund", "NoSQL", "MukuDB", "Mukund-Database"],
    install_requires=[],
    python_requires="~=3.7",
)