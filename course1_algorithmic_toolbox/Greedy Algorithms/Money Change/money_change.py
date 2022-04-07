# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    coins = [10, 5, 1]
    n_coins = 0
    for coin in coins:
        n_coins += money // coin
        money = money % coin

    return n_coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
