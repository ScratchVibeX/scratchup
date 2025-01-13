from setuptools import setup, find_packages

setup(
    name='scratchup',
    version='1.0.0',
    description='An advanced Python library for interacting with Scratch\'s APIs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='ScratchVibeX',,
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
