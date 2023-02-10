# This file is placed in the Public Domain.


import json
import os
import unittest


from opv.decoder import ObjectDecoder, load, loads
from opv.encoder import dumps
from opv.objects import Object, oid


VALIDJSON = '{"test": "bla"}'


class TestDecoder(unittest.TestCase):

    def test_loads(self):
        obj = Object()
        obj.test = "bla"
        oobj = loads(dumps(obj))
        self.assertEqual(oobj.test, "bla")

