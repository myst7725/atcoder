S = input()
l = len(S)
ans = ""
for i in range(0,l,2):
    ans += S[i+1]+S[i]
print(ans)
