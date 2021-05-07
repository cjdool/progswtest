def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for k in range(m+n-1):
        for i in range(k+1):
            j = k - i
            if 0 <= i < n and 0 <= j < m:
                if [j+1, i+1] in puddles:
                    continue
                if j != 0:
                    dp[i][j] += dp[i][j-1]
                if i != 0:
                    dp[i][j] += dp[i-1][j]
                dp[i][j] = dp[i][j] % 1000000007
    return dp[n-1][m-1]


print(solution(4, 3, [[2, 2]]))
