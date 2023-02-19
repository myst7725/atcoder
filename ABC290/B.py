N, K = map(int,input().split())
S = input()

ans = ""
for i in range(N):
    s = S[i]
    if s == "o" and K>0:
        ans += "o"
        K = K-1
    else:
        ans += "x"
print(ans)

