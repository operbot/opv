# This file is placed in the Public Domain.


def cmd(event):
    print(",".join(sorted(event.target.cmds)))
