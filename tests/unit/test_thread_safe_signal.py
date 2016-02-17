"""
Unit tests.
"""

from mock import (
    MagicMock,
    call,
)
from pytest import mark
from threading import Thread

from pyslot import ThreadSafeSignal as Signal

with_emit_arguments = mark.parametrize('args,kwargs', [
    ([], {}),
    ([1], {}),
    ([], {'a': 2}),
    ([1], {'a': 2}),
])


@with_emit_arguments
def test_signal_emit_no_connection(args, kwargs):
    signal = Signal()
    signal.emit(*args, **kwargs)


@with_emit_arguments
def test_signal_emit_single_connection(args, kwargs):
    callback = MagicMock()
    signal = Signal()
    signal.connect(callback)

    signal.emit(*args, **kwargs)
    callback.assert_called_once_with(*args, **kwargs)


@with_emit_arguments
def test_signal_emit_double_connection(args, kwargs):
    callbacks = [MagicMock(), MagicMock()]
    signal = Signal()

    for callback in callbacks:
        signal.connect(callback)

    signal.emit(*args, **kwargs)

    for callback in callbacks:
        callback.assert_called_once_with(*args, **kwargs)


@with_emit_arguments
def test_signal_emit_multiple_connection(args, kwargs):
    callback = MagicMock()
    signal = Signal()

    for _ in range(3):
        signal.connect(callback)

    signal.emit(*args, **kwargs)

    assert callback.mock_calls == [
        call(*args, **kwargs)
        for _ in range(3)
    ]


@with_emit_arguments
def test_signal_emit_after_disconnect(args, kwargs):
    cb = MagicMock()

    def callback(*args, **kwargs):
        cb(*args, **kwargs)

    signal = Signal()
    signal.connect(callback)
    signal.disconnect(callback)

    signal.emit(*args, **kwargs)

    assert cb.mock_calls == []


@with_emit_arguments
def test_signal_emit_after_implicit_disconnect(args, kwargs):
    def callback(): pass
    signal = Signal()
    signal.connect(callback)
    del callback

    assert not signal.callbacks

    signal.emit(*args, **kwargs)


@with_emit_arguments
def test_disconnect_during_emit(args, kwargs):
    signal = Signal()

    def remover(*args, **kwargs):
        signal.disconnect(remover)

    callbacks = [MagicMock(), remover, MagicMock(), MagicMock()]

    for callback in callbacks:
        signal.connect(callback)

    signal.emit(*args, **kwargs)

    for callback in callbacks:
        if callback is not remover:
            callback.assert_called_once_with(*args, **kwargs)


@with_emit_arguments
def test_simultaneous_emit(args, kwargs):
    callback = MagicMock()
    signal = Signal()
    signal.connect(callback)

    NUM_THREADS = 20

    threads = [
        Thread(target=signal.emit, args=args, kwargs=kwargs)
        for _ in range(NUM_THREADS)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    assert callback.mock_calls == [
        call(*args, **kwargs)
        for _ in range(NUM_THREADS)
    ]
