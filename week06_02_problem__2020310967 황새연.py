S = [5, 2, 3, 4, 6]

def matrix_chain(S):
    
    n=len(S)
    dp = [[0 for i in range(n)] for j in range(n)]

    for a in range(2, n):
        for i in range(1, n-a+1):
            j = i+a-1
            dp[i][j] = 100000 #max값 설정
            for k in range(i, j):
                q = dp[i][k] + dp[k+1][j] + S[i-1] * S[k] * S[j]
                if dp[i][j] > q: #min값 반환
                    dp[i][j]=q

    return dp[1][n-1]

print("The minimum number of operations =", matrix_chain(S))
