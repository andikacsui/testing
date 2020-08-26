
class SortAndCombine:

    def __init__(self):
        self.result = []

    def sort_and_combine(self, input_1, input_2):

        if not(all(isinstance(i, int) for i in input_1) and isinstance(input_1, list)):
            raise ValueError('input_1 must be a list with integer in all values')
        elif not (all(isinstance(i, str) for i in input_2) and isinstance(input_2, list)):
            raise ValueError('input_2 must be a list with string in all values')

        input_1 = sorted(input_1)
        input_2 = sorted(input_2, key=str.casefold) # only valid in Python 3.
                                                    # For python 2 use: sorted(input_2, key=lambda i: i.lower())

        for i in range(max(len(input_1), len(input_2))):

            self.result.append('[{}:{}]'.format(input_1[i] if i < len(input_1) else 'NULL',
                                                input_2[i] if i < len(input_2) else 'NULL'))

        return ','.join(self.result)


if __name__ == "__main__":

    sac = SortAndCombine()
    input_1 = [4, 3, 6, 5, 1, 2] # list of integer
    input_2 = ['F', 'C', 'D', 'B', 'A'] # list of string
    print(sac.sort_and_combine(input_1, input_2))
