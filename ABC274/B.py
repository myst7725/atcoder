import numpy as np
H, W = map(int,input().split())
C = [[] for _ in range(W)]
for i in range(H):
    c = input()
    for j in range(W):
        C[j].append(c[j])

ans = []
for cc in C:
    ans.append(cc.count("#"))

print(*ans)
