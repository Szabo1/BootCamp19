import unittest

from prime_number2 import prime_number



class Prime_numberTest(unittest.TestCase):

	#check for number below 2 and return false

	#if number in range is divisible by two break

	#if number is prime append to empty list

	def test_prime_number(self):

		expected = [2, 3, 5]

		self.assertEqual( prime_number(7),expected)

		



if __name__ == '__main__':

	unittest.main()