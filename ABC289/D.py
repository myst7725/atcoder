N = int(input())
A = set(map(int,input().split()))
M = int(input())
B = set(map(int,input().split()))
X = int(input())

DP = [0 for _ in range(X+1)]
DP[0] = 1

for now in range(X+1):
    if now in B:
        pass
    else:
        if DP[now] == 1:
            for a in A:
                after = now+a
                if X < after:
                    pass
                else:
                    DP[after] = 1

if DP[X] == 1:
    print("Yes")
else:
    print("No")
    











