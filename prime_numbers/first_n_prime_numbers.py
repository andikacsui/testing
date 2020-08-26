class FindNPrimeNumbers:

    def __init__(self):
        self.found = 0
        self.current = 2
        self.result = []

    def find_prime_numbers(self, total):
        '''
        Find the first n prime numbers based on the input

        :param total: total prime numbers to be retrieved
        :return: list of the prime numbers
        '''

        if not isinstance(total, int) or total < 0:
            raise ValueError('Input must be a zero or a positive integer')

        while self.found < total:

            if self.current <= 3:

                self.result.append(self.current)
                self.found += 1


            elif not (self.current % 2 == 0 or self.current % 3 == 0):

                i = 5

                while i * i <= self.current:
                    if self.current % i == 0 or self.current % (i + 2) == 0:
                        break
                    i += 6

                if i * i > self.current:
                    self.result.append(self.current)
                    self.found += 1

            self.current += 1

        return self.result


if __name__ == "__main__":

    fnpn = FindNPrimeNumbers()
    total = 4
    print(fnpn.find_prime_numbers(total))