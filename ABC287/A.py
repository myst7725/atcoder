N = int(input())
For = 0
for i in range(N):
    s = input()
    if s == "For":
        For += 1

if For > N//2:
    print("Yes")
else:
    print("No")
