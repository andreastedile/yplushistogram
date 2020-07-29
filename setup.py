from setuptools import setup, find_packages
from os import path

setup(
    name='yplushistogram',
    version='1.0',
    author='Andrea Stedile',
    author_email='andrea.stedile@studenti.unitn.it',
    packages=find_packages(),
    scripts=[path.join('yplushistogram', 'yplushistogram')],
    install_requires=['PyQt5', 'PyQtChart']
)
