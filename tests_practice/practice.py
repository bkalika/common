from math import log
from typing import List, Any, Union


# class DiverseTasks:
#     def __init__(self, word=None, number=None, number_digits=None, zero=None, progression=None, numbers=None,
#                  missing_number=None, ttuple=None, reversed_word=None, clock=None,
#                  l_word=None):
#         self.word = word
#         self.number = number
#         self.number_digits = number_digits
#         self.zero = zero
#         self.progression = progression
#         self.numbers = numbers
#         self.missing_number = missing_number
#         self.ttuple = ttuple
#         self.reversed_word = reversed_word
#         self.clock = clock
#         self.l_word = l_word

def task1_common_numbers(a, b) -> list:
    return list(set(a) & set(b))


def task2_find_count_a(some_str) -> int:
    while 'a' in some_str:
        return some_str.count('a')


def task3_power_of_three(number) -> int:
    x: float = log(number, 3)
    return int(x) == log(number, 3)


def task4_add_digits(digits) -> int:
    while digits > 9:
        digits_count = sum(int(i) for i in str(digits))
        if digits_count <= 9:
            return digits_count
        digits = digits_count


def task5_zero_in_the_end(zero) -> int:
    for elem in zero:
        if elem == 0:
            zero.remove(elem)
            zero.append(elem)
    return zero


def task6_arithmetic_progression(progression) -> bool:
    if len(progression) < 2:
        return False
    diff = progression[1] - progression[0]
    count = 1
    while count < len(progression)-1:
        if progression[count+1] != progression[count] + diff:
            return False
        count += 1
        return True


def task7_not_occur_twice(numbers) -> str:
    for num in numbers:
        if numbers.count(num) == 1:
            return num


def task8_missing_number(missing_number) -> list:
    num: set = set(range(1, max(missing_number)))
    new_list: set = set(missing_number)
    return list(num.difference(new_list))


def task9_is_tuple(tuple_) -> int:
    new_list: list = []
    for elem in tuple_:
        if type(elem) == tuple:
            break
        new_list.append(elem)
    return new_list[-1]


def task10_reversed_words(reversed_word) -> str:
    return reversed_word[::-1]


def task11_clock(clock) -> str:
    hours: int = clock // 60
    minutes: int = clock % 60
    return f"{hours}:{minutes}"


def task12_longest_word(l_word) -> str:
    new_word: str = l_word.split()
    return max(new_word, key=len)


def task13_input_word(input_string) -> str:
    r_words: str = input_string.split()
    r_words.reverse()
    r_words = " ".join(r_words)
    return r_words


def task14_fibonacci(fibonacci) -> Union[list, int]:
    new_list: list = [1, 1]
    if fibonacci == 1:
        return new_list[0]
    elif fibonacci == 2:
        return new_list
    else:
        for i in range(1, fibonacci-1):
            new_list.append(new_list[-1] + new_list[-2])
        return new_list


def task15_even_numbers(a: list) -> list:
    return [elem for elem in a if elem % 2 == 0]


def task16_add_up_numbers(up_numbers) -> int:
    # input_number: int = int(input("Enter number: "))
    new_list: list = [1]
    for elem in range(2, up_numbers+1):
        new_list.append(elem)
        elem += 1
    return sum(new_list)


def task17_factorial(input_number: int) -> int:
    if input_number < 2:
        return 1
    else:
        return input_number*(task17_factorial(input_number - 1))


def task18_replace_latter() -> str:
    vowel: list = ["a", "e", "i", "o", "u"]
    input_sms: str = "abcd"
    new_word: list = []
    new_words: list = []
    for letter in input_sms:
        new_word.append(chr(ord(letter)+1))
    for word in new_word:
        if word in vowel:
            new_words.append(word.upper())
        else:
            new_words.append(word)
    return "".join(new_words)


def task19_sort_words(input_words) -> str:
    new_words: list = sorted(input_words)
    return "".join(new_words)


def task20_equal_two_parameters(input_1, input_2) -> Union[bool, int]:
    if input_1 < input_2:
        return True
    elif input_1 == input_2:
        return -1
    else:
        return False
