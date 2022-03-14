# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def larger_combination(number1, number2):
    comb1 = int(str(number1) + str(number2))
    comb2 = int(str(number2) + str(number1))

    if comb1 >= comb2:
        return True
    else:
        return False


def largest_number(numbers):
    maximum_number = ""
    while True:
        if len(numbers) == 0:
            return int(maximum_number)
        number = 0
        for i in range(len(numbers)):
            number1 = numbers[i]
            if larger_combination(number1, number):
                number = number1
                count = i

        maximum_number += str(number)
        numbers.pop(count)









if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))

