N = int(input())
X = list(map(int,input().split()))
X.sort()

newX = X[N:-N]
sum_newX = sum(newX)
number = 3*N
ans = sum_newX/number
print(ans)