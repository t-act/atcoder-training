# https://atcoder.jp/contests/abc098/tasks/arc098_a

# input
n = int(input())
s = list(input())


# method
w_count = 0
e_count = s.count("E")
ans = 10**18

# リーダーを一人ずつやってみる
for ss in s:
    if ss == "E":
        e_count -= 1
    ans = min(ans, w_count+e_count)
    if ss == "W":
        w_count += 1

print(ans)

# countがO(N)なためNG
# # リーダーを一人ずつ割り当ててみる
# for i in range(n):
#     # リーダーを挟んで左側の(W)をカウント、右側のEをカウント
#     if i == 0:
#         e_count = s[1:].count("E")
#         w_count = 0
#     elif i == n-1:
#         w_count = s[:-1].count("W")
#         e_count = 0
#     else:
#         w_count = s[:i].count("W")
#         e_count = s[i+1:].count("E")

#     # カウントが小さければ更新
#     count = e_count + w_count
#     if count < ans:
#         ans = count

