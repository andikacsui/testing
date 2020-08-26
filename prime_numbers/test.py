import unittest
import first_n_prime_numbers

class FindNPrimeNumbersTest(unittest.TestCase):

    def setUp(self):

        self.fnpn = first_n_prime_numbers.FindNPrimeNumbers()

        # zero input
        self.zero_number = 0
        self.zero_result = []

        # small_case
        self.small_number = 10
        self.small_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        # large case
        self.large_number = 100
        self.large_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                             89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
                             181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
                             281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
                             397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                             503, 509, 521, 523, 541]

        # total result
        self.check_total = 99

    def test_zero_case(self):

        self.assertEqual(self.fnpn.find_prime_numbers(self.zero_number), self.zero_result)

    def test_small_case(self):

        self.assertEqual(self.fnpn.find_prime_numbers(self.small_number), self.small_result)

    def test_large_case(self):

        self.assertEqual(self.fnpn.find_prime_numbers(self.large_number), self.large_result)

    def test_result_len(self):

        self.assertEquals(len(self.fnpn.find_prime_numbers(self.check_total)), self.check_total)

if __name__ == '__main__':
    unittest.main()
