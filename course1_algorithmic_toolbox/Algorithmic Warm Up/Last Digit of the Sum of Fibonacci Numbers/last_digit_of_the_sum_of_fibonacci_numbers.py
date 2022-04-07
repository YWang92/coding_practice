# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

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


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    period_numbers = fibonacci_number_again(n, 10)
    len_period = len(period_numbers)

    a = (n + 1) // len_period
    b = (n + 1) % len_period

    solution = a * sum(period_numbers) + sum(period_numbers[:b])
    solution = solution % 10

    return solution


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))

