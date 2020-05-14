import sys


def dp_change(money, coins):
    MinNumCoins = [0]
    for m in range(1, money + 1):
        MinNumCoins.append(money + 1)
        for coin in coins:
            if m >= coin:
                current = MinNumCoins[m - coin] + 1
                if current < MinNumCoins[m]:
                    MinNumCoins[m] = current
    return MinNumCoins[money]


if __name__ == "__main__":
    '''
    Given: An integer money and an array Coins of positive integers.
    Return: The minimum number of coins with denominations Coins that changes money.
    '''
    input_lines = sys.stdin.read().splitlines()
    money = int(input_lines[0])
    Coins = [int(x) for x in input_lines[1].split(",")]

    print(dp_change(money, Coins))
