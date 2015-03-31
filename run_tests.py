# !/usr/bin/env python2
# coding: utf-8

import sys
import unittest
from tests.auth_test import AuthTestCase
from tests.create_topic_test import CreateTopicTestCase


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTestCase),
        unittest.makeSuite(CreateTopicTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
