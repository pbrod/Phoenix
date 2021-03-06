#!/usr/bin/env python

__author__ = "Patrick K. O'Brien <pobrien@orbtech.com>"

import unittest

from wx.py import pseudo


"""
These unittest methods are preferred:
-------------------------------------
self.assert_(expr, msg=None)
self.assertEqual(first, second, msg=None)
self.assertRaises(excClass, callableObj, *args, **kwargs)
self.fail(msg=None)
self.failIf(expr, msg=None)
"""


class ModuleTestCase(unittest.TestCase):

    def test_module(self):
        module = pseudo
        self.assert_(module.__author__)
        self.assert_(module.PseudoFile)
        self.assert_(module.PseudoFileErr)
        self.assert_(module.PseudoFileIn)
        self.assert_(module.PseudoFileOut)
        self.assert_(module.PseudoKeyword)


class PseudoTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


class PseudoFileTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


class PseudoFileOutTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _write(self):
        pass

    def test_PseudoFileOut_goodInit(self):
        self.assert_(pseudo.PseudoFileOut(write=self._write))

    def test_PseudoFileOut_badInit(self):
        self.assertRaises(ValueError, pseudo.PseudoFileOut, write='bad')


if __name__ == '__main__':
    unittest.main()
