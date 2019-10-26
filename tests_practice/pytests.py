import pytest
from unittest import mock

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
                task20_equal_two_parameters
                )


def setup():
    task1_list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    task1_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    a = "I am a good developer. I am also a writer"
    number = 9
    digits = 48
    zero = [0, 2, 0, 4, 4, 6, 7, 10]
    progression = [5, 7, 9, 11]
    numbers = [5, 3, 4, 3, 4]
    missing_number = [1, 2, 3, 4, 6, 7, 8, 10, 15]
    tuple_ = [1, 2, 3, 7, 9, (1, 2), 3]
    reversed_word = "Hello World and Coders"
    clock = 63
    longest_word = "I love your mind"
    input_string = "My name is Michele"
    fibonacci = 7
    even_numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    factorial = 4
    input_word = "edcba"
    up_numbers = 4
    one = 10
    one_ = 12
    two = 12
    two_ = 10
    three = 5
    three_ = 5


def test_task1_common_numbers():
    # task1 = DiverseTasks("I am a good developer. I am also a writer")
    assert task1_common_numbers(task1_list1) == [1, 2, 3, 5, 8, 13]


def test_task2_find_count_a():
    task2 = DiverseTasks("I am a good developer. I am also a writer")
    assert task2.task2_find_count_a() == 5


def test_task3_power_of_three():
    task3 = DiverseTasks(number=9)
    assert task3.task3_power_of_three()


def test_task4_add_digits():
    task4 = DiverseTasks(number_digits=482)
    assert task4.task4_add_digits() == 5


def test_task5_zero_in_the_end():
    end_zero = [2, 4, 4, 6, 7, 10, 0, 0]
    task5 = DiverseTasks(zero=[0, 2, 0, 4, 4, 6, 7, 10])
    assert task5.task5_zero_in_the_end() == end_zero


def test_task6_arithmetic_progression():
    task6 = DiverseTasks(progression=[5, 7, 9, 11])
    assert task6.task6_arithmetic_progression()


def test_task7_not_occur_twice():
    task7 = DiverseTasks(numbers=[5, 3, 4, 3, 4])
    assert task7.task7_not_occur_twice() == 5


def test_task8_missing_number():
    expected = [5, 9, 11, 12, 13, 14]
    task8 = DiverseTasks(missing_number=[1, 2, 3, 4, 6, 7, 8, 10, 15])
    assert task8.task8_missing_number() == expected


def test_task9_missing_number():
    task9 = DiverseTasks(ttuple=[1, 2, 3, 7, 9, (1, 2), 3])
    assert task9.task9_is_tuple() == 9


def test_task10_reversed_words():
    expected = "sredoC dna dlroW olleH"
    task10 = DiverseTasks(reversed_word="Hello World and Coders")
    assert task10.task10_reversed_words() == expected


def test_task11_clock():
    expected = '1:3'
    task11 = DiverseTasks(clock=63)
    assert task11.task11_clock() == expected


def test_task12_longest_word():
    expected = 'love'
    task12 = DiverseTasks(l_word="I love your mind")
    assert task12.task12_longest_word() == expected


def test_task13_input_word():
    expected = "Michele is name My"
    with mock.patch('builtins.input', return_value="My name is Michele"):
        assert task13_input_word() == expected


def test_task14_fibonacci():
    expected = [1, 1, 2, 3, 5, 8, 13]
    with mock.patch('builtins.input', return_value=7):
        assert task14_fibonacci() == expected


def test_task15_even_numbers():
    expected = [4, 16, 36, 64, 100]
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert task15_even_numbers(a) == expected


def test_task16_add_up_numbers():
    with mock.patch('builtins.input', return_value=4):
        assert task16_add_up_numbers() == 10


def test_task17_factorial():
    assert task17_factorial(4) == 24


def test_task18_replace_letter():
    output = "bcdE"
    assert task18_replace_latter() == output


def test_task19_sort_words():
    input_word = task19_sort_words("edcba")
    assert task19_sort_words('abcde') == input_word


def test_task20_equal_two_parameters():
    assert task20_equal_two_parameters(10, 12)
    assert not task20_equal_two_parameters(12, 10)
    assert task20_equal_two_parameters(5, 5)


if __name__ == "__main__":
    pytest.main()
