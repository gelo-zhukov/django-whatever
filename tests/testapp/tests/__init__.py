import doctest
import os
import sys
from glob import glob
from unittest import TestSuite, defaultTestLoader

TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))


def suite():
    result = TestSuite()

    result.addTest(doctest.DocTestSuite('django_any.xunit'))
    result.addTest(doctest.DocTestSuite('django_any.forms'))

    for filename in glob(os.path.join(TESTS_ROOT, '*.py')):
        if filename.endswith('__init__.py'):
            continue

        module_name = 'testapp.tests.%s' % \
                      os.path.splitext(os.path.basename(filename))[0]
        __import__(module_name)

        result.addTest(
            defaultTestLoader.loadTestsFromModule(sys.modules[module_name]))

    return result
