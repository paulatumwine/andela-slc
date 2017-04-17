import unittest


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
