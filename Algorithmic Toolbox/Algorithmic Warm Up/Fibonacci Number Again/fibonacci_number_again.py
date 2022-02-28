# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


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

    period = len(fibo_numbers)
    return fibo_numbers[n % period] % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))


