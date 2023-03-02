# This file is placed in the Public Domain.


import sys
import time


from opv.objects import Object
from opv.storage import Storage
from opv.utility import elapsed, fntime


def __dir__():
    return (
            'Log',
            'log',
           )


class Log(Object):

    def __init__(self):
        super().__init__()
        self.txt = ""


Storage.add(Log)


def log(event):
    if not event.rest:
        nmr = 0
        for fnm, obj in sorted(Storage.find("log"), key=lambda x: fntime(x[0])):
            event.reply("%s %s %s" % (
                                nmr,
                                obj.txt,
                                elapsed(time.time() - fntime(fnm)))
                               )
            nmr += 1
        return
    obj = Log()
    obj.txt = event.rest
    Storage.save(obj)
    event.reply("ok")
