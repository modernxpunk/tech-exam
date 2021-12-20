import unittest
from main import Main

class TestMain(unittest.TestCase):
	def setUp(self):
		self.a = 10
		self.b = 2
		self.calc = Main(self.a, self.b)

	def test_plus(self):
		self.assertEqual(self.calc.plus(), self.a + self.b)

	def test_minus(self):
		self.assertEqual(self.calc.minus(), self.a - self.b)

	def test_multiply(self):
		self.assertEqual(self.calc.multiply(), self.a * self.b)

	def test_divide(self):
		self.assertEqual(self.calc.divide(), self.a // self.b)

if __name__ == '__main__':
	import xmlrunner
	runner = xmlrunner.XMLTestRunner(output="test-reports")
	unittest.main(testRunner=runner)
	unittest.main()