# test_calc.py
import unittest
from calc import add, div

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)  # ✅ 通过时绿色

    def test_add_fail(self):
        self.assertEqual(add(1, 2), 4)  # ❌ 失败时红色

    def test_div(self):
        self.assertEqual(div(6, 3), 2)  # ✅

    def test_div_zero(self):
        with self.assertRaises(ZeroDivisionError):  # ✅
            div(1, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)