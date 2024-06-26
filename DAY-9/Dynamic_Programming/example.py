def memoisation(n):
    if n <= 1:
        return n
    return memoisation(n - 1) + memoisation(n - 2)


def tabulation(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


n = 10
memo = memoisation(n)
tabu = tabulation(n)
print(memo)
print(tabu)
