N = int(input())
A = list(map(int,input().split()))
D = {1:0}

for i in range(1, len(A)+1):
    Ai = A[i-1]
    DAi = D[Ai]
    D[2*i] = DAi+1
    D[2*i+1] = DAi+1

D = dict(sorted(D.items()))

for value in D.values():
    print(value)
