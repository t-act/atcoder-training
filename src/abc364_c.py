# https://atcoder.jp/contests/abc364/tasks/abc364_c

# input
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# method
def sort_add_loop(l: list, threshold: int) -> int:
    count = 0
    total_score = 0
    for ll in sorted(l, reverse=True):
        count += 1
        total_score += ll
        if total_score > threshold:
            break
    return count

a_num = sort_add_loop(a, x)
b_num = sort_add_loop(b, y)

# Nが2e5なので場合分けはいらない↓ (1e9を超える場合はNG)

# # xとyどちらが小さいかを判定, x = y の場合は
# if x == y:
#     # a, bを降順ソート
#     # a, bの要素を数える -> n
#     # max(a), max(b)
#     pass

# # xのほうが小さい場合、aだけ見る
# elif x < y:
#     # aを降順ソート、
#     # xを超えるまで足す、
#     ans_count = sort_add_loop(a, x)
    
# # yのほうが小さい場合、bだけ見ればいい
# else:
#     # bを降順ソート、
#     # yを超えるまで足す、
#     ans_count = sort_add_loop(b, y)



# 足した回数(max(n)回)を出力
print(min(a_num, b_num))