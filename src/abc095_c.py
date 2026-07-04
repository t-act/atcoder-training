# https://atcoder.jp/contests/abc095/tasks/arc096_a
# 全探索

a, b, c, x, y = map(int, input().split())

# 5パターンを試す、最小値を出力

# 1. AとBだけ購入
single = (a*x) + (b*y)

# 2. ABだけ
if x == y:
    multi = c*2*x

# 3. AとAB
elif x > y:
    multi = (c*(2*y)) + (a*(x - y))

# 4. BとAB
elif y > x:
    multi = (c*(2*x)) + (b*(y - x))

# 5. ABだけ（あまり有り）
surplus = c * 2*max(x,y)

print(min(single, multi, surplus))