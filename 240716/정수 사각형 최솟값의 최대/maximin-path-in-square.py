n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

def init():
    dp[0][0] = arr[0][0]
    for i in range(1,n):
        dp[0][i] = arr[0][i]
    for i in range(1,n):
        dp[i][0] = arr[i][0]
init()

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(min(dp[i-1][j] ,arr[i][j]), min(dp[i][j-1] ,arr[i][j]))
print(dp[-1][-1])