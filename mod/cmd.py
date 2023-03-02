# This file is placed in the Public Domain.


from opv.listens import Listens


def cmd(event):
    bot = Listens.byorig(event.orig)
    event.reply(",".join(sorted(bot.cmds)))
