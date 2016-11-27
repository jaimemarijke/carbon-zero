import os

from setuptools import find_packages, setup

setup(
    name='carbon-zero',
    version='0.0.' + os.environ.get('BUILD_NUMBER', '0'),
    description='Carbon footprint calculator',
    maintainer='Jaime McCandless',
    maintainer_email='jaime.m.mccandless@gmail.com',
    url='carbonzero.me',
    packages=find_packages(exclude=('tests',)),
    entry_points={
        'console_scripts': [
            'send-email = carbon_zero.email:send',
        ]
    },
    install_requires=(
        'requests',
    ),
    include_package_data=True,   # See MANIFEST.in
)
