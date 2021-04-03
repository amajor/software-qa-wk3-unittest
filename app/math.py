class Math:
    def add(self, a: int, b: int):
        '''calculates and returns a plus b'''
        return a + b

    def multiply(self, a: int, b: int):
        '''calculates and returns a multiplied by b'''
        return a * b

    def divide(self, a: int, b: int):
        ''' calculates a divided by b, raises ValueError on division by Zero'''
        if b == 0:
            raise ValueError

        return a / b

    def is_even(self, a: int):
        # The // operator rounds the result down to the nearest whole number.
        # It is for FLOOR DIVISION. It yields the quotient.
        # We actually want the remainder. If the remainder is 0 when divided by 2, it's even.
        # Use the modulo instead of floor division.
        # return a // 2 == 0  <-- FLOOR DIVISION
        return a % 2 == 0   # <-- MODULO

    def power(self, a: int, b: int):
        '''calculates a to the power of b'''
        prod = 1
        for i in range(abs(b)):
            prod *= a

        return prod

    def is_prime(self, num: int):
        '''finds out if num is a prime or not'''
        if num < 0:
            raise (ValueError())
        if num == 0:
            return False

        if num <= 3:
            return True

        for i in range(2, num):
            if num % i == 0:
                return False

        return True

    def factorial(self, n: int):
        '''calculates n! = 1 * 2 * 3 * ... * n'''

        '''We should raise an error if a negative value is passed in'''
        if n < 0:
            raise (ValueError())

        prod = 1
        for i in range(1, n + 1):
            prod *= i

        return prod

    def factors(self, number: int):
        '''finds and returns list of factors for number'''
        if number <= 0:
            raise ValueError('number must be greater than zero')
        if number == 1 or number == 2:
            return list(range(1, number + 1))

        factors = [1, number]
        for factor in range(2, number):
            if number % factor == 0:
                factors.append(factor)

        return factors
