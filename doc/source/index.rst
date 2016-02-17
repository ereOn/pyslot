.. _index:

PySlot - Documentation
======================

`PySlot` a dead-simple signal/slot library for Python.

Installation
------------

You may install it by using `pip`::

   pip install pyslot

Basic usage
-----------

`PySlot` provides two signal classes:

* :class:`Signal <pyslot.Signal>` for basic signals in mono-threaded code.
* :class:`ThreadSafeSignal <pyslot.ThreadSafeSignal>` for cross-thread signal
  instance usage.

Both have the same interface and can be used like so:

.. code-block::
   python

   from pyslot import Signal

   def greet(name, msg):
      print("{name} says: {msg}".format(name=name, msg=msg))

   signal = Signal()
   signal.connect(greet)

   signal.emit("alice", msg="Hi Bob !")
   signal.emit("bob", msg="Hi Alice !")

The :func:`connect <pyslot.Signal.connect>` function stores a reference (which
can be strong or weak) to any callable that will in turn be called whenever the
:func:`emit <pyslot.Signal.emit>` method gets called.

A signal can be connected to several callables, which will all be called *in
their registration order*.

It is also possible to disconnect a callable from the signal by calling the
:func:`disconnect <pyslot.Signal.disconnect>` method with that callable as the
single argument. If only a weak-reference to the callable is kept,
destroying the callable will implicitely disconnect it from the signal as well.

.. note::
   No matter what variant of the `Signal` class you use, it is **always** safe
   for a callable to call :func:`disconnect <pyslot.Signal.disconnect>`, be it
   for itself or for another callable.

Table of contents
=================

.. toctree::
   :maxdepth: 2

   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
