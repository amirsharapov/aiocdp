from setuptools import setup, find_packages

setup(
    name='pycdp',
    version='0.0.1',
    packages=find_packages(
        include=[
            'pycdp',
            'pycdp.*'
        ],
        exclude=[
            'tests',
            'tests.*'
        ]
    ),
    install_requires=[
    ]
)
