# This file is placed in the Public Domain.


import json
import os
import unittest


from opv.encoder import ObjectEncoder, dumps
from opv.objects import Object, oid


VALIDJSON = '{"test": "bla"}'


class TestEncoder(unittest.TestCase):


    def test_dumps(self):
        obj = Object()
        obj.test = "bla"
        self.assertEqual(dumps(obj), VALIDJSON)
