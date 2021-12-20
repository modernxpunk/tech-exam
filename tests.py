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
		self.assertEqual(ans, [fib(i) for i in range(-3, 10)])

if __name__ == '__main__':
	import xmlrunner
	runner = xmlrunner.XMLTestRunner(output="test-reports")
	unittest.main(testRunner=runner)
	unittest.main()