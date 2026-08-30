n = int(input("Enter number of coins: "))

coins = []

for i in range(n):
    coin = int(input("Enter coin denomination: "))
    coins.append(coin)

amount = int(input("Enter target amount: "))

dp = [[0] * (amount + 1) for i in range(n + 1)]

for i in range(1, amount + 1):
    dp[0][i] = float('inf')

for i in range(1, n + 1):

    for a in range(1, amount + 1):

        if coins[i - 1] <= a:

            take = 1 + dp[i][a - coins[i - 1]]
            not_take = dp[i - 1][a]

            dp[i][a] = min(take, not_take)

        else:
            dp[i][a] = dp[i - 1][a]

if dp[n][amount] == float('inf'):
    print("Amount cannot be formed")
else:
    print("Minimum number of coins:", dp[n][amount])
