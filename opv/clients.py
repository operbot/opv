# This file is placed in the Public Domain.


from .handler import Handler
from .listens import Listens
from .message import Message


class Client(Handler):

    def __init__(self):
        Handler.__init__(self)
        Listens.add(self)

    def announce(self, txt):
        self.raw(txt)

    def event(self, txt):
        msg = Message()
        msg.orig = repr(self)
        msg.parse(txt)
        return msg

    def raw(self, txt):
        pass

    def say(self, channel, txt):
        self.raw(txt)
