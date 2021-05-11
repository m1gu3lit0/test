import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        num = 10
        result = main.make_some(num)
        self.assertEqual(result,15)


if __name__ == '__main__':
    unittest.main()