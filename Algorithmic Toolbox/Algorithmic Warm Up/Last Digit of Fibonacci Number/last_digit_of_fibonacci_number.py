# python3

def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    a, b = 0, 1
    fibo_numbers_last_digit = [a % 10, b % 10]
    for _ in range(n):
        a, b = b % 10, (a+b) % 10
        fibo_numbers_last_digit.append(b)

    return fibo_numbers_last_digit[n]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
