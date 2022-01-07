import django
import os
from django.test.utils import setup_test_environment, teardown_test_environment


class BaseTest(django.test.TestCase):
    @classmethod
    def setUpClass(cls):
        teardown_test_environment()
        os.environ['DJANGO_SETTINGS_MODULE'] = 'shop_list.tests.settings'
        django.setup()
        super().setUpClass()
        setup_test_environment()
        from shop_list import models
        cls.models = models
