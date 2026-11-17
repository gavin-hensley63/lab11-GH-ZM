# https://github.com/gavin-hensley63/lab11-GH-ZM
# Partner 1: Gavin Hensley
# Partner 2: Zijian Mao


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 4), 4)
        self.assertEqual(add(-2, 3), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(3, 8), -5)
        self.assertEqual(subtract(0, 0), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1, 2), 2)
        self.assertEqual(mul(9, 3), 27)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(1, 8), 8)
        self.assertEqual(div(25, 100), 4)
        self.assertEqual(div(2, 1), 1/2)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(8, 2), 3)
        self.assertEqual(logarithm(9, 3), 2)
        self.assertEqual(logarithm(16, 2), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 6)

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     call log function inside, example:
    #     with self.assertRaises(<INSERT_ERROR_TYPE>):
    #         logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 100)
            logarithm(1, 100)
            logarithm(5, 0)
            logarithm(100, 1)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(20, 21), 29)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
