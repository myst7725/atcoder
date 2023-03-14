N, Q = map(int,input().split())
card = [0]*N
for _ in range(Q):
    #event
    c, x = map(int,input().split())

    if c == 1:
        card[x-1]+=1

    elif c == 2:
        card[x-1]+=2
    
    else:
        if 2 <= card[x-1]:
            print("Yes")
        else:
            print("No")



