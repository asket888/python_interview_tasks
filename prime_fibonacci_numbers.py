"""Write an application which takes an integer number as an input (num).
Return a list of 'num' primary elements from fibonacci sequence starting from beginning
e.g: Given: fibonacci sequence "0, 1, 1, 2, 3, 5, 8, 13, 21, ..."
     When: user type '4' as application input
     Then: application returns [2, 3, 5, 13]"""


import time
import unittest


def fibonacci(prime_elements_num: int):
    if type(prime_elements_num) != int:
        raise NonIntInputException
    if prime_elements_num == 0:
        raise WrongInputParameterException("Input parameter should be greater than 0")
    if prime_elements_num > 9:
        raise WrongInputParameterException("Cause of performance issue, input parameter should be less than 10. "
                                           "We are working on finding the reasons and will try to keep you updated "
                                           "on the news")
    prime_elements_list = []
    fibonacci_pair = [1, 2]

    while len(prime_elements_list) < prime_elements_num:
        first = fibonacci_pair[0]
        second = fibonacci_pair[1]
        if all(second % i for i in range(2, second)):
            prime_elements_list.append(second)
        fibonacci_pair = [second, first + second]

    return prime_elements_list


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_happy_path(self):
        self.assertTrue(fibonacci(5), [2, 3, 5, 13, 89])

    def test_fibonacci_non_int_input_validation(self):
        self.assertRaises(NonIntInputException, lambda: fibonacci("5"))

    def test_fibonacci_zero_input_validation(self):
        with self.assertRaises(WrongInputParameterException) as error:
            fibonacci(0)
        self.assertEqual(str(error.exception), "Input parameter should be greater than 0")

    def test_fibonacci_maximum_input_validation(self):
        with self.assertRaises(WrongInputParameterException) as error:
            fibonacci(10)
        self.assertEqual(str(error.exception), "Cause of performance issue, input parameter should be less than 10. "
                                               "We are working on finding the reasons and will try to keep you updated "
                                               "on the news")

    def test_fibonacci_performance(self):
        millis_before_test = int(round(time.time() * 1000))
        fibonacci(9)
        millis_after_test = int(round(time.time() * 1000))
        method_speed = millis_after_test - millis_before_test
        print(method_speed)
        self.assertLess(method_speed, 50)


class NullInputException(Exception):
    pass


class NonIntInputException(Exception):
    pass


class WrongInputParameterException(Exception):
    pass


if __name__ == '__main__':
    unittest.main()