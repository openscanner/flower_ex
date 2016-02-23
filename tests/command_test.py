#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest


TEST_CONFIG = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_config.cson")


class AppExLoaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_read_config(self):
        pass



if __name__ == '__main__':
    unittest.main()
