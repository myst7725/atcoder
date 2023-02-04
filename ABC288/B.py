N , K = map(int,input().split())
S = [input() for _ in range(N)]
SK = S[:K]
SK.sort()
for k in range(K):
    print(SK[k])