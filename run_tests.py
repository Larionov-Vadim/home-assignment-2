#!/usr/bin/env python2

import sys
import unittest
from tests.create_topic_test import CreateTopicTestCase


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CreateTopicTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
