import unittest


def generate_primes(number):
	"""
	A function to generate prime numbers from 0 to number
	
	This function has a worst case runtime of O(n2) because 
	i has to get to number for the function to terminate
	"""
	
    number_types = (int, float, complex)

    if not isinstance(number, number_types):
        raise ValueError

    i = 1
    factors = 0
    primes = []
    while i < number:

        j = 1
        while j <= i:
            if i % j == 0 and (j != 1 or j != number):
                factors += 1
            j += 1

        if factors == 2:
            primes.append(i)

        i += 1
        factors = 0

    return primes


class TestGeneratePrimes(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_primes_returns_correct_result(self):
        self.assertEqual([2, 3, 5, 7], generate_primes(10))

    def test_generate_primes_does_not_return_zero(self):
        self.assertNotIn(0, generate_primes(10))

    def test_generate_primes_does_not_return_one(self):
        self.assertNotIn(1, generate_primes(10))

    def test_generate_primes_only_allows_positive_input(self):
        self.assertRaises(ValueError, generate_primes, -10)
        self.assertRaises(ValueError, generate_primes, 0)

    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, generate_primes, "ten")


if __name__ == '__main__':
    unittest.main()
