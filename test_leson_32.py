import unittest

import leson_32


class Test_leson_32(unittest.TestCase):
    def test_examination(self):
        self.assertEqual(leson_32.examination(10, 10), 1)
        self.assertEqual(leson_32.examination(12, 0))
