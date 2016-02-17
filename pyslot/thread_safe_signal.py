"""
The base signal classes.
"""

from weakref import ref
from threading import RLock


class ThreadSafeSignal(object):
    """
    A thread-safe signal implementation.

    ..note:: This class is thread-safe. You may connect, disconnect or emit the
        signal from different threads.
    """
    def __init__(self):
        self._callbacks = []
        self._read_lock = RLock()
        self._write_lock = RLock()

    def connect(self, callback):
        """
        Connects a new callback to this signal.

        :param callback: The callback to connect.

        `callback` will be called whenever `emit` gets called on the `Signal`
        instance. A weak reference is kept, meaning that if the callback gets
        destroyed, it is unregistered from the signal automatically. This
        design choice helps avoiding circular references in user-code.

        ..note:: Connecting the same callback twice or more will cause the
            callback to be called several times per `emit` call.
        """
        with self._write_lock:
            with self._read_lock:
                self._callbacks.append(ref(callback, self._disconnect))

    def _disconnect(self, callback_ref):
        with self._write_lock:
            with self._read_lock:
                self._callbacks.remove(callback_ref)

    def disconnect(self, callback):
        """
        Disconnects a callback from this signal.

        :param callback: The callback to disconnect.

        ..warning:: If the callback is not connected at the time of call, an
            `ValueError` exception is thrown.

        ..note:: You may call `disconnect` from a connected callback.
        """
        self._disconnect(ref(callback))

    @property
    def callbacks(self):
        with self._read_lock:
            return [callback_ref() for callback_ref in self._callbacks]

    def emit(self, *args, **kwargs):
        """
        Emit the signal.

        :param args: The arguments.
        :param kwargs: The keyword arguments.
        """
        for callback in self.callbacks:
            callback(*args, **kwargs)
