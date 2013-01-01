#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def run_setup():
    setup(
        name='sql-to-graphite',
        version='0.0.1',
        description='A tool to send SQL results to Graphite',
        keywords = 'SQL Graphite',
        url='http://github.com/philipcristiano/sql-to-graphite',
        author='Philip Cristiano',
        author_email='philipcristiano@gmail.com',
        license='BSD',
        packages=['sql_to_graphite'],
        install_requires=[
            'sqlalchemy',
            'mysql-python',
        ],
        test_suite='tests',
        long_description=read('README.md'),
        zip_safe=True,
        classifiers=[
        ],
        entry_points="""
        [console_scripts]
        sql-to-graphite=sql:main
        """,
    )

if __name__ == '__main__':
    run_setup()
