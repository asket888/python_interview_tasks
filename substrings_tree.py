import unittest


def solution(input_string):
    """Solution for the task itself
    :param input_string: input string that should be verified
    :return: returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers
    """
    __check_validation(input_string)
    substrings = __get_all_possible_substrings(base_string=input_string)
    best_by_leftovers = __get_candidates_best_by_leftovers_count(substrings=substrings, base_string=input_string)
    best_by_quantity = __get_candidates_best_by_elements_count(substrings=best_by_leftovers)
    return best_by_quantity[0][1]


def __check_validation(input_string):
    """Checks that input parameters match to all requirements described in the task
    :param input_string: input string that should be verified
    """
    if not input_string:
        raise NullInputException("Input string should be not empty")
    if type(input_string) != str:
        raise NonStringInputException("Input value should be a string")
    if len(input_string) >= 200:
        raise TooLongInputException("Input string should be less than 200 characters")
    for i in input_string:
        if not i.isalpha():
            raise NonStringInputException("All input value characters should be an alpha")


def __get_all_possible_substrings(base_string):
    """Returns all possible substrings from string
    :param base_string: base string where substrings should be found
    :return: substrings as a list()
    """
    substrings = []
    for n in range(1, len(base_string) + 1):
        for i in range(len(base_string) - n + 1):
            substrings.append(base_string[i:i + n])
    return substrings


def __get_candidates_best_by_leftovers_count(substrings, base_string):
    """Returns all candidates sorted by leftovers_count parameter
    :param base_string: base string where substrings should be found
    :param substrings: all possible substrings in base_string parameter
    :return: candidates as a sorted list([substring, substring_count, leftovers_count])
    """
    candidates = []
    for element in substrings:
        elements_count = base_string.count(element)
        leftovers_count = len(base_string.replace(element, ""))
        candidates.append([element, elements_count, leftovers_count])
    candidates.sort(key=lambda x: x[2])
    return candidates


def __get_candidates_best_by_elements_count(substrings):
    """Returns all candidates sorted by substring_count parameter
    :param substrings: all possible substrings in base_string parameter
    :return: candidates as a sorted list([substring, substring_count, leftovers_count])
    """
    candidates = []
    best_leftover = substrings[0][2]
    for element in substrings:
        if element[2] == best_leftover:
            candidates.append(element)
    candidates.sort(reverse=True, key=lambda x: x[1])
    return candidates


class TestSolution(unittest.TestCase):

    def test_solution_happy_path_case_1(self):
        self.assertTrue(solution("abcabcabcabc"), 4)

    def test_solution_happy_path_case_2(self):
        self.assertTrue(solution("abccbaabccba"), 2)

    def test_solution_non_string_input_validation(self):
        with self.assertRaises(NonStringInputException) as error:
            solution(123)
        self.assertEqual(str(error.exception), "Input value should be a string")

    def test_solution_non_alpha_character_validation(self):
        with self.assertRaises(NonStringInputException) as error:
            solution("ab1")
        self.assertEqual(str(error.exception), "All input value characters should be an alpha")

    def test_solution_zero_input_validation(self):
        with self.assertRaises(NullInputException) as error:
            solution("")
        self.assertEqual(str(error.exception), "Input string should be not empty")

    def test_solution_maximum_input_validation(self):
        with self.assertRaises(TooLongInputException) as error:
            solution("abcd" * 50)
        self.assertEqual(str(error.exception), "Input string should be less than 200 characters")


class NullInputException(Exception):
    pass


class NonStringInputException(Exception):
    pass


class TooLongInputException(Exception):
    pass
