# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    candy, sum_candy = 1, 0
    while True:
        if sum_candy + candy > n:
            break
        sum_candy += candy
        summands.append(candy)
        candy += 1

    summands[-1] += (n - sum_candy)

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
