"""
A dead-simple signal/slot library for Python.
"""

from .signal import Signal
from .thread_safe_signal import ThreadSafeSignal

__all__ = [
    'Signal',
    'ThreadSafeSignal',
]
