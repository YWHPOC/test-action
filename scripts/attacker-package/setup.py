from setuptools import setup, find_packages

setup(
    name='my_poc_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # add dependencies here if needed
    entry_points={
        'console_scripts': [
            'run-poc=my_poc_package.main:run',  # Entry point for the command
        ],
    },
)
