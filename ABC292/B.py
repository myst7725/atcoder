N = int(input())
A = list(map(int,input().split()))
C = [0]*N

for i in range(N):
    if C[i]==1:
        pass
    else:
        a = A[i]
        C[a-1] = 1

print(C.count(0))
X = []
for i in range(N):
    if C[i] == 0:
        X.append(i+1)
    else:
        pass
print(*X)


