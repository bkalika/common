import unittest

from practice import (
                task1_common_numbers,
                task2_find_count_a,
                task3_power_of_three,
                task4_add_digits,
                task5_zero_in_the_end,
                task6_arithmetic_progression,
                task7_not_occur_twice,
                task8_missing_number,
                task9_is_tuple,
                task10_reversed_words,
                task11_clock,
                task12_longest_word,
                task13_input_word,
                task14_fibonacci,
                task15_even_numbers,
                task16_add_up_numbers,
                task17_factorial,
                task18_replace_latter,
                task19_sort_words,
                task20_equal_two_parameters,
                )


class TestPractice(unittest.TestCase):

    def setUp(self) -> None:
        self.task1_list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.task1_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.a = "I am a good developer. I am also a writer"
        self.number = 9
        self.digits = 48
        self.zero = [0, 2, 0, 4, 4, 6, 7, 10]
        self.progression = [5, 7, 9, 11]
        self.numbers = [5, 3, 4, 3, 4]
        self.missing_number = [1, 2, 3, 4, 6, 7, 8, 10, 15]
        self.tuple_ = [1, 2, 3, 7, 9, (1, 2), 3]
        self.reversed_word = "Hello World and Coders"
        self.clock = 63
        self.longest_word = "I love your mind"
        self.input_string = "My name is Michele"
        self.fibonacci = 7
        self.even_numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.factorial = 4
        self.input_word = "edcba"
        self.up_numbers = 4
        self.one = 10
        self.one_ = 12
        self.two = 12
        self.two_ = 10
        self.three = 5
        self.three_ = 5

    def test_task1_common_numbers(self):
        actual = task1_common_numbers(self.task1_list1, self.task1_list2)
        expected = [1, 2, 3, 5, 8, 13]
        self.assertEqual(actual, expected)

    def test_task2_find_count_a(self):
        self.assertEqual(task2_find_count_a(self.a), 5)

    def test_task3_power_of_three(self):
        self.assertTrue(task3_power_of_three(self.number))

    def test_task4_add_digits(self):
        self.assertEqual(task4_add_digits(self.digits), 3)

    def test_task5_zero_in_the_end(self):
        end_zero = [2, 4, 4, 6, 7, 10, 0, 0]
        self.assertEqual(task5_zero_in_the_end(self.zero), end_zero)

    def test_task6_arithmetic_progression(self):
        self.assertTrue(task6_arithmetic_progression(self.progression))

    def test_task7_not_occur_twice(self):
        self.assertEqual(task7_not_occur_twice(self.numbers), 5)

    def test_task8_missing_number(self):
        expected = [5, 9, 11, 12, 13, 14]
        self.assertEqual(task8_missing_number(self.missing_number), expected)

    def test_task9_not_tuple(self):
        self.assertEqual(task9_is_tuple(self.tuple_), 9)

    def test_task10_reversed_words(self):
        expected = "sredoC dna dlroW olleH"
        self.assertEqual(task10_reversed_words(self.reversed_word), expected)

    def test_task11_clock(self):
        expected = '1:3'
        self.assertEqual(task11_clock(self.clock), expected)

    def test_task12_longest_word(self):
        expected = 'love'
        self.assertEqual(task12_longest_word(self.longest_word), expected)

    def test_task13_input_word(self):
        expected = "Michele is name My"
        self.assertEqual(task13_input_word(self.input_string), expected)

    def test_task14_fibonacci(self):
        expected = [1, 1, 2, 3, 5, 8, 13]
        self.assertEqual(task14_fibonacci(self.fibonacci), expected)

    def test_task15_even_numbers(self):
        expected = [4, 16, 36, 64, 100]
        self.assertEqual(task15_even_numbers(self.even_numbers), expected)

    def test_task16_add_up_numbers(self):
        self.assertEqual(task16_add_up_numbers(self.up_numbers), 10)

    def test_task17_factorial(self):
        self.assertEqual(task17_factorial(self.factorial), 24)

    def test_task18_replace_letter(self):
        output = "bcdE"
        self.assertEqual(task18_replace_latter(), output)

    def test_task19_sort_words(self):
        self.assertEqual(task19_sort_words(self.input_word), 'abcde')

    def test_task20_equal_two_parameters(self):
        self.assertTrue(task20_equal_two_parameters(self.one, self.one_))
        self.assertFalse(task20_equal_two_parameters(self.two, self.two_))
        self.assertEqual(task20_equal_two_parameters(self.three, self.three_), -1)


if __name__ == "__main__":
    unittest.main()
