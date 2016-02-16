"""
The base signal classes.
"""

from weakref import ref


class Signal(object):
    """
    The base signal class.
    """
    def __init__(self):
        self.callbacks = []

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
        self.callbacks.append(ref(callback, self.callbacks.remove))

    def disconnect(self, callback):
        """
        Disconnects a callback from this signal.

        :param callback: The callback to disconnect.

        ..note:: If the callback is not connected at the time of call, an
            `ValueError` exception is thrown.
        """
        self.callbacks.remove(ref(callback))

    def emit(self, *args, **kwargs):
        """
        Emit the signal.

        :param args: The arguments.
        :param kwargs: The keyword arguments.
        """
        for callback in self.callbacks:
            callback()(*args, **kwargs)
