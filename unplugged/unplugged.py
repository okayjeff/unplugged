import unittest

from unplugged.patcher import Patcher
import settings


def setup_patchers():
    """
    Generate a list of patched objects, one patcher for each object that is
    responsible for sending an HTTP request.
    """
    return [Patcher(target) for target in settings.PATCH_TARGETS]


def start_patchers(patchers):
    for patcher in patchers:
        patcher.start()


def stop_patchers(patchers):
    for patcher in patchers:
        patcher.stop()


class UnpluggedTestCase(unittest.TestCase):
    patchers = setup_patchers()

    @classmethod
    def setUpClass(cls):
        super(UnpluggedTestCase, cls).setUpClass()
        start_patchers(cls.patchers)

    @classmethod
    def tearDownClass(cls):
        super(UnpluggedTestCase, cls).tearDownClass()
        stop_patchers(cls.patchers)
