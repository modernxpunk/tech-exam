import unittest
from main import fib

class TestMain(unittest.TestCase):
	def test_fibNegative(self):
		self.assertEqual(fib(-10), None)

	def test_fibZero(self):
		self.assertEqual(fib(0), 0)

	def test_fibPositive(self):
		self.assertEqual(fib(5), 5)

	def test_fibAllCases(self):
		ans = []
		for i in range(-3, 10):
			ans.append(fib(i))
		self.assertEqual(ans, [None, None, None, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == '__main__':
	import xmlrunner
	runner = xmlrunner.XMLTestRunner(output="test-reports")
	unittest.main(testRunner=runner)
	unittest.main()