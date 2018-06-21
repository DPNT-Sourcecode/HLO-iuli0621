import unittest

from solutions.HLO.hello_solution import hello


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(hello("x"), "Hello, World!")


if __name__ == '__main__':
    unittest.main()
