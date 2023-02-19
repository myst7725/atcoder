N = int(input())
for i in range(N+1):
    if i == 0:
        f = 1
    else:
        f = f*i
print(f)