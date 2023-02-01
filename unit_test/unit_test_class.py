import unittest

class Test(unittest.TestCase):
    def setUp(self):
        print("set up called")
        self.a=10
        self.b=20

    def test_sum_func1(self):
        print("test1 called")
        result = self.a + self.b
        print(result)
        self.assertEqual(result, self.a+self.b)

    def test_sum_func2(self):
        print("test2 called")
        result = self.b + self.a
        self.assertEqual(result, self.a+self.b)

if __name__ == "__main__":
    unittest.main()