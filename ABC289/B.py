N , M = map(int,input().split())
A = list(map(int,input().split()))
ans = []
memo = []
C = 0


while True:
    C += 1
    if C == N+1:
        print(*ans)
        break
    else:
        if C in A:
            memo.append(C)
        else:
            ans += [C] + memo[::-1]
            memo = []
            #print(C, ans)