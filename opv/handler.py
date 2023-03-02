# This file is placed in the Public Domain.


import importlib
import inspect
import os
import queue
import threading
import time


from .objects import Object, update
from .threads import launch


def __dir__():
    return (
            'Handler',
           ) 


__all__ = __dir__()


class Handler(Object):

    def __init__(self):
        Object.__init__(self)
        self.cmds = Object()
        self.queue = queue.Queue()
        self.stopped = threading.Event()

    def event(self, txt):
        splitted = txt.split()
        event = Object()
        event.args = []
        event.cmd = ""
        event.rest = ""
        if splitted:
            event.cmd = splitted.pop(0)
        if splitted:
            event.args = splitted
            event.rest = " ".join(splitted)
        event.target = self
        return event

    def handle(self, event):
        if not event or "cmd" not in event:
            return
        func = getattr(self.cmds, event.cmd, None)
        if not func:
            return
        return func(event)

    def loop(self):
        while not self.stopped.set():
            self.handle(self.poll())

    def poll(self):
        return self.queue.get()

    def put(self, event):
        self.queue.put_nowait(event)

    def register(self, func):
        setattr(self.cmds, func.__name__, func)

    def scan(self, mod):
        for key, cmd in inspect.getmembers(mod, inspect.isfunction):
            if "event" in cmd.__code__.co_varnames:
                self.register(cmd)

    def start(self):
        launch(self.loop)

    def wait(self):
        while not self.stopped:
            time.sleep(1.0)
