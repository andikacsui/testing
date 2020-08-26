import unittest
import sort_and_combine

class FindNPrimeNumbersTest(unittest.TestCase):

    def setUp(self):

        self.sac = sort_and_combine.SortAndCombine()

        # normal case
        self.input_1_normal = [1, 2, 3, 4, 5]
        self.input_2_normal = ['a', 'b', 'c', 'd', 'e']
        self.expected_output_normal = '[1:a],[2:b],[3:c],[4:d],[5:e]'

        # empty input list
        self.input_1_empty = []
        self.input_2_empty = []
        self.expected_output_empty = ''

        # Inputs length are different
        self.input_1_diff = [100]
        self.input_2_diff = ['x', 'y', 'z']
        self.expected_output_diff = '[100:x],[NULL:y],[NULL:z]'

        # Unsorted inputs
        self.input_1_unsorted = [500, 200, 400, 100]
        self.input_2_unsorted = ['Z', 'A', 'K', 'Y']
        self.expected_output_unsorted = '[100:A],[200:K],[400:Y],[500:Z]'

        # Mix case input_2 string
        self.input_1_mix = [1, 2, 3, 4]
        self.input_2_mix = ['a', 'B', 'c', 'D']
        self.expected_output_mix = '[1:a],[2:B],[3:c],[4:D]'


    def test_normal_case(self):

        self.assertEquals(self.sac.sort_and_combine(self.input_1_normal, self.input_2_normal),
                          self.expected_output_normal)

    def test_empty_case(self):

        self.assertEquals(self.sac.sort_and_combine(self.input_1_empty, self.input_2_empty),
                          self.expected_output_empty)

    def test_different_len_case(self):

        self.assertEquals(self.sac.sort_and_combine(self.input_1_diff, self.input_2_diff),
                          self.expected_output_diff)

    def test_unsorted_case(self):

        self.assertEquals(self.sac.sort_and_combine(self.input_1_unsorted, self.input_2_unsorted),
                          self.expected_output_unsorted)

    def test_mix_case(self):

        self.assertEquals(self.sac.sort_and_combine(self.input_1_mix, self.input_2_mix),
                          self.expected_output_mix)


if __name__ == '__main__':
    unittest.main()
