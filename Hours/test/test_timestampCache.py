import datetime
import os
import time

from cache import TimestampCache
from unittest import TestCase


class TestTimestampCache(TestCase):
    time_format = "%Y-%m-%d %H:%S"
    test_time = "2016-11-21 23:24"
    cache = None

    def setUp(self):
        self.cache = TimestampCache()
        self.cache.file_name = "\\test.cache"

    def tearDown(self):
        self.cache = None

    @classmethod
    def setUpClass(cls):
        try:
            os.remove(os.path.dirname(os.path.abspath(__file__ + "\\..\\test.cache")))
        except OSError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove(os.path.dirname(os.path.abspath(__file__ + "\\..\\test.cache")))
        except OSError:
            pass

    def test_save_timestamp(self):
        self.cache.save_timestamp(time.mktime(datetime.datetime.strptime(self.test_time, self.time_format).timetuple()))

    def test_load_timestamp(self):
        save_time_obj = self.cache.load_timestamp()
        test_time_obj = time.mktime(datetime.datetime.strptime(self.test_time, self.time_format).timetuple())
        self.assertEqual(test_time_obj, save_time_obj)
