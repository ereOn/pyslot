from setuptools import (
    setup,
    find_packages,
)

setup(
    name='pyslot',
    author='Julien Kauffmann',
    author_email='julien.kauffmann@freelan.org',
    maintainer='Julien Kauffmann',
    maintainer_email='julien.kauffmann@freelan.org',
    version=open('VERSION').read().strip(),
    url='http://ereOn.github.io/pyslot',
    description=(
        "A dead-simple signal/slot implementation for Python."
    ),
    long_description="""\
PySlot is a super simple signal/slot library for Python designed for speed and
ease-of-use.
""",
    packages=find_packages(exclude=[
        'tests',
    ]),
    install_requires=[
        'six>=1.10.0,<2.0.0',
    ],
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 5 - Production/Stable',
    ],
)
