# https://atcoder.jp/contests/tessoku-book/tasks/dp_a

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
print(step[n-1])