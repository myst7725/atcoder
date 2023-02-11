import itertools

N, M = map(int,input().split())
C = []
S = []
for _  in range(M):
    c = int(input())
    C.append(c)
    s = set(map(int,input().split()))
    S.append(s)

ans = 0
A = set(i for i in range(1, N+1))

for m in range(1, M+1):
    SM = itertools.combinations(S, m)
    for sm in SM:
        print(sm)
        B = set()
        for sm1 in sm:
            B = B.union(sm1)
        if A == B:
            ans += 1
print(ans)






    



