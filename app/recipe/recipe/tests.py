from django.test import SimpleTestCase

from recipe import utils


class Test_Clac(SimpleTestCase):
    def test_add_numbers(self):
        res = utils.calc(5, 5)

        self.assertEqual(res, 10)

    def test_subtract_numbers(self):
        res = utils.subtract(10, 5)

        self.assertEquals(res, 5)
