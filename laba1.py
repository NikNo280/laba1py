import sys
import argparse
import random

def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if (namespace.number_func == 1):
        word_count(namespace.argument)
        print(word_count(namespace.argument))
    elif (namespace.number_func == 2):
        quick_sort(namespace.argument)
    elif (namespace.number_func == 3):
        merge_sort(namespace.argument)
    elif (namespace.number_func == 4):
        fibonacci_factory(int(namespace.argument))


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('number_func', choices=[1, 2, 3, 4], type=int, default=4)
    parser.add_argument('argument', default=10)
    return parser


def word_count(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        text_str = file.read().lower()
        updated_text_str = ""
        for i in text_str:
            if ((i <= "я" and i >= "а") or (i == " ") or (i <= "z" and i >= "a") or (i == "-")):
                updated_text_str += i
        arr_str = updated_text_str.split(" ")
        dictionary = {}

        for index in range(0, len(arr_str)):
            str = arr_str[index]

            if(str != ''):
                if(dictionary.get(str) == None):
                    dictionary[str] = 1
                else:
                    dictionary[str] = dictionary[str] + 1

        arr_str = sorted(dictionary.items(), key=lambda count: count[1])
        print(arr_str)
        dictionary = dict(arr_str[-10:])
        arr_str = list(dictionary.keys())
        print(' '.join(arr_str))
        return ' '.join(arr_str)


def fibonacci(n):
    fib1 = 0
    fib2 = 1
    for i in range(n):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        yield fib1


def fibonacci_factory(n):
    for fib in fibonacci(n):
        print(fib, end=" ")


def algoritm_quick_sort(array, left_range, right_range):
    sup_arg = array[int(left_range + (right_range - left_range) / 2)]
    i = left_range
    j = right_range

    while i <= j:
        while array[i] < sup_arg:
            i = i + 1
        while array[j] > sup_arg:
            j = j - 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i = i + 1
            j = j - 1

    if left_range < j:
        algoritm_quick_sort(array, left_range, j)
    if right_range > i:
        algoritm_quick_sort(array, i, right_range)


def quick_sort(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        arr_number = list(map(int, file.read().split(" ")))
    print(arr_number)
    algoritm_quick_sort(arr_number, 0, len(arr_number) - 1)
    print(arr_number)

def algoritm_merge_sort(array):
    if len(array) < 2:
        return array
    else:
        middle = int(len(array) / 2)
        left = algoritm_merge_sort(array[:middle])
        right = algoritm_merge_sort(array[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        arr_number = list(map(int, file.read().split(" ")))
    print(arr_number)
    print(algoritm_merge_sort(arr_number))
    pass


main()