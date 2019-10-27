import pytest


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


task1_list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
task1_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
count_a = "I am a good developer. I am also a writer"
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
sort_letters = "edcba"
one = 10
one_ = 12
two = 12
two_ = 10
three = 5
three_ = 5


@pytest.mark.parametrize('list1, list2', [(task1_list1, task1_list2)])
def test_task1_common_numbers(list1, list2):
    exp = [1, 2, 3, 5, 8, 13]
    assert task1_common_numbers(list1, list2) == exp


@pytest.mark.parametrize('count_letter_a', [count_a])
def test_task2_find_count_a(count_letter_a):
    assert task2_find_count_a(count_a) == 5


@pytest.mark.parametrize('three_power', [number])
def test_task3_power_of_three(three_power):
    assert task3_power_of_three(number)


@pytest.mark.parametrize('sum_digits', [digits])
def test_task4_add_digits(sum_digits):
    assert task4_add_digits(digits) == 3


@pytest.mark.parametrize('list_end_zero', [zero])
def test_task5_zero_in_the_end(list_end_zero):
    end_zero = [2, 4, 4, 6, 7, 10, 0, 0]
    assert task5_zero_in_the_end(zero) == end_zero


@pytest.mark.parametrize('ar_progression', [progression])
def test_task6_arithmetic_progression(ar_progression):
    assert task6_arithmetic_progression(progression)


@pytest.mark.parametrize('single', [numbers])
def test_task7_not_occur_twice(single):
    assert task7_not_occur_twice(numbers) == 5


@pytest.mark.parametrize('miss_number', [missing_number])
def test_task8_missing_number(miss_number):
    expected = [5, 9, 11, 12, 13, 14]
    assert task8_missing_number(missing_number) == expected


@pytest.mark.parametrize('not_tuple', tuple_)
def test_task9_not_tuple(not_tuple):
    assert task9_is_tuple(tuple_) == 9


@pytest.mark.parametrize('revers_string', [reversed_word])
def test_task10_reversed_words(revers_string):
    expected = "sredoC dna dlroW olleH"
    assert task10_reversed_words(reversed_word) == expected


@pytest.mark.parametrize('watch', [clock])
def test_task11_clock(watch):
    expected = '1:3'
    assert task11_clock(clock) == expected


@pytest.mark.parametrize('long_word', [longest_word])
def test_task12_longest_word(long_word):
    expected = 'love'
    assert task12_longest_word(longest_word) == expected


@pytest.mark.parametrize('input_sentence', input_string)
def test_task13_input_word(input_sentence):
    expected = "Michele is name My"
    assert task13_input_word(input_string) == expected


@pytest.mark.parametrize('fibonacci_number', [fibonacci])
def test_task14_fibonacci(fibonacci_number):
    expected = [1, 1, 2, 3, 5, 8, 13]
    assert task14_fibonacci(fibonacci) == expected


@pytest.mark.parametrize('even_number', [even_numbers])
def test_task15_even_numbers(even_number):
    expected = [4, 16, 36, 64, 100]
    assert task15_even_numbers(even_numbers) == expected


@pytest.mark.parametrize('add_numbers', [up_numbers])
def test_task16_add_up_numbers(add_numbers):
    assert task16_add_up_numbers(up_numbers) == 10


@pytest.mark.parametrize('find_factorial', [factorial])
def test_task17_factorial(find_factorial):
    assert task17_factorial(factorial) == 24


@pytest.mark.parametrize('replace', input_word)
def test_task18_replace_letter(replace):
    output = "bcdE"
    assert task18_replace_latter() == output


@pytest.mark.parametrize('sort', sort_letters)
def test_task19_sort_words(sort):
    correct = "abcde"
    assert task19_sort_words(sort_letters) == correct


@pytest.mark.parametrize('equal', [(one, one_), (two, two_), (three, three_)])
def test_task20_equal_two_parameters(equal):
    assert task20_equal_two_parameters(one, one_)
    assert not task20_equal_two_parameters(two, two_)
    assert task20_equal_two_parameters(three, three_)


if __name__ == "__main__":
    pytest.main()
