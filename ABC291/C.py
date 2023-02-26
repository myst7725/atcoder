N = int(input())
S = input()

stage = {(0, 0)}
now_x, now_y = 0, 0
ans = "No"

for s in S:
    #移動
    if s == "R":
        now_x += 1
    elif s == "L":
        now_x -= 1
    elif s == "U":
        now_y += 1
    else:
        now_y -= 1
    
    #確認
    now = (now_x, now_y)
    if now in stage:
        ans = "Yes"
        break
    else:
        stage.add(now)

# print(stage)
print(ans)




