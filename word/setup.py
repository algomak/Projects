import os.path
from setuptools import find_packages, setup

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')) as f:
    long_description = '\n' + f.read()

setup(
    name='dict',
    version='0.1.0',
    description='',
    long_description=long_description,
    url='https://github.com/algomak/Projects/tree/master/word',
    packages=find_packages(exclude=('tests',)),
    python_requires='>=3.6.0',
    install_requires=[
        'attrs==17.4.0',
        'requests==2.31.0',
        'attr==0.3.1'
    ],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    entry_points={'console_scripts': ['dict = cli:main']},
)
