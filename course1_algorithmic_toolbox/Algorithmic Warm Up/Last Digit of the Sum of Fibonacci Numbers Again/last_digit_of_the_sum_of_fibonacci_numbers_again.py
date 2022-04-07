# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def fibonacci_number_again(m):
    a, b = 0, 1
    fibo_numbers = [a, b]
    while True:
        a, b = b, a+b
        if a % m == 0 and b % m == 1:
            fibo_numbers.pop()
            break
        else:
            fibo_numbers.append(b)

    return fibo_numbers


def the_sum_of_fibonacci_numbers(n):

    period_numbers = fibonacci_number_again(10)
    len_period = len(period_numbers)

    a = (n + 1) // len_period
    b = (n + 1) % len_period

    solution = a * sum(period_numbers) + sum(period_numbers[:b])

    return solution


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    from_index_sum = the_sum_of_fibonacci_numbers(from_index - 1)
    to_index_sum = the_sum_of_fibonacci_numbers(to_index)

    solution = (to_index_sum - from_index_sum) % 10

    return solution


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
