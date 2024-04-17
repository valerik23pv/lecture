from setuptools import setup
from io import open

version = '1.0.0'

long_decription = '''a new python peoject'''

setup(
    name='project_1',
    version=version,

    author='vetkav',
    author_email='soofy230@gmail.com',
    description='desk',

    long_description=long_decription,
    url='https://github.com/valerik23pv/lecture.git',

    #download_url=,
    license='none',
    packages=['project_1'],
    install_requires=['flask'],
    classifiers=['', '']


)