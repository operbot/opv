# This file is placed in the Public Domain.


import os
import pathlib
import time


def __dir__():
    return (
            'cdir',
            'fnclass',
            'fntime',
            'locked',
           )


__all__ = __dir__()


def cdir(path):
    pth = pathlib.Path(path)
    if path.split(os.sep)[-1].count(":") == 2:
        pth = pth.parent
    os.makedirs(pth, exist_ok=True)


def fnclass(path):
    try:
        _rest, *pth = path.split("store")
        splitted = pth[0].split(os.sep)
        return splitted[1]
    except ValueError:
        pass
    return None


def fntime(daystr):
    daystr = daystr.replace("_", ":")
    datestr = " ".join(daystr.split(os.sep)[-2:])
    if "." in datestr:
        datestr, rest = datestr.rsplit(".", 1)
    else:
        rest = ""
    tme = time.mktime(time.strptime(datestr, "%Y-%m-%d %H:%M:%S"))
    if rest:
        tme += float("." + rest)
    else:
        tme = 0
    return tme


def locked(lock):

    def lockeddec(func, *args, **kwargs):

        if args or kwargs:
            locked.noargs = True

        def lockedfunc(*args, **kwargs):
            lock.acquire()
            res = None
            try:
                res = func(*args, **kwargs)
            finally:
                lock.release()
            return res

        lockedfunc.__wrapped__ = func
        lockedfunc.__doc__ = func.__doc__
        return lockedfunc

    return lockeddec
