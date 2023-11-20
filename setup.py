from setuptools import setup, find_packages

setup(
    name='aiocdp',
    version='0.0.1',
    packages=find_packages(
        include=[
            'aiocdp',
            'aiocdp.*'
        ],
        exclude=[
            'tests',
            'tests.*'
        ]
    ),
    install_requires=[
        'websockets',
        'requests',
    ]
)
