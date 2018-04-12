from setuptools import setup, find_packages

setup(
    name='pyidenticon',
    version='0.0.1',
    description='A identicon python implementation.',
    author='jeremaihloo',
    author_email='jeremaihloo1024@gmail.com',
    url='https://github.com/jeremaihloo/pyidenticon',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # entry_points={
    #     'console_scripts': [
    #         'hottings=hottings:main',
    #     ],
    # },
    install_requires=[
        'pillow',
    ],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/jeremaihloo/pyidenticon/issues',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/jeremaihloo/pyidenticon',
    },
)