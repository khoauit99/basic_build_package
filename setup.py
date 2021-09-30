from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', encoding="utf-8-sig") as f:
    requirements = f.readlines()

setup(
    name = "khoa1409",
    #packages = ["src"],
    description='A python implementation of OpenNMT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version= '14.09',

    package_dir = {'':"src"},

    packages= find_packages(where= 'src'),

    install_requires=requirements,

    entry_points = {
        "console_scripts" : [
            "khoa_hello=khoa_lib:main",
            "khoa_plus=khoa_lib.khoa_plus:main",
        ],
    },
)