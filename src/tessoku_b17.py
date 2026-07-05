# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cp

n = int(input())
h = list(map(int, input().split()))

step = {0: 0, 1: abs(h[1]-h[0])}
normal = 0
skip = 0

for i in range(2,n):
    normal = abs(h[i] - h[i-1]) + step[i-1]
    skip = abs(h[i] - h[i-2]) + step[i-2]

    if skip <= normal:
        step[i] = skip
    else:
        step[i] = normal
    # print(f"{i=}, {step=}")

footing = n-1
ans = [n]  # 最後の足場は必ず踏む

# 最後の足場から逆算する
while footing > 2:
    # i-1で式成立なら足場は1個戻す
    if step[footing] == step[footing-1] + abs(h[footing] - h[footing-1]):
        footing -= 1
    # i-2で式成立なら足場は2個戻す
    else:
        footing -= 2
    ans.append(footing+1)
    # print(f"{footing=}, {ans=}")

# 最初の足場(i=1)があるかを判定、なければ1を追加
if 1 not in ans:
    ans.append(1)

# 最後の足場からのリストになっているので、リバースして提出
print(len(ans))
print(*reversed(ans))