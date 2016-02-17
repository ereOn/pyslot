[![Build Status](https://travis-ci.org/ereOn/pyslot.svg?branch=master)](https://travis-ci.org/ereOn/pyslot)
[![Coverage Status](https://coveralls.io/repos/ereOn/pyslot/badge.svg?branch=master&service=github)](https://coveralls.io/github/ereOn/pyslot?branch=master)
[![Documentation Status](https://readthedocs.org/projects/pyslot/badge/?version=latest)](http://pyslot.readthedocs.org/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/pyversions/pyslot.svg)](https://pypi.python.org/pypi/pyslot/1.0.0)
[![GitHub tag](https://img.shields.io/github/tag/ereOn/pyslot.svg)](https://github.com/ereOn/pyslot)
[![PyPi version](https://img.shields.io/pypi/v/pyslot.svg)](https://pypi.python.org/pypi/pyslot/1.0.0)
[![PyPi downloads](https://img.shields.io/pypi/dm/pyslot.svg)](https://pypi.python.org/pypi/pyslot/1.0.0)

# PySlot

**PySlot** is a dead-simple signal/slot library for Python.

## Usage

An example is worth a thousand words:

    from pyslot import Signal

    signal = Signal()

    def greet(name, msg):
        print("{name} says: {msg}".format(name=name, msg=msg))

    signal.connect(greet)

    signal.emit("alice", "Hello Bob !")
    signal.emit("bob", "Hello Alice !")

The `Signal` class is simple, optimized and straightforward. It synchronously
calls all the connected callbacks, in order, whenever its `emit` method get
called.

Learn more about it in the
[documentation](https://readthedocs.org/projects/pyslot/badge/?version=latest).

## Installation

You may install it by using `pip`:

> pip install pyslot
