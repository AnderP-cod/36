import unittest
import fn
import leson_32


class Testfn(unittest.TestCase):
    def test_add(self):
        self.assertEqual(fn.add(10, 20), 30)

    def test_subtract(self):
        self.assertEqual(fn.subtract(2, 2), 0)

    def test_multiply(self):
        self.assertEqual(fn.multiply(2, 2), 4)


