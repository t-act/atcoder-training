# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l

def check(x, n, k, a):
    """指定時間xで出力される合計枚数がk以上でTrueを返す"""
    sum = 0
    for i in range(n):
        sum += x // a[i]  # x: [s], a: [s/枚]
    if sum >= k:
        return True
    else:
        return False


n, k = map(int, input().split())
a = list(map(int, input().split()))

left = 1
right = 10 ** 9
while left < right:
    mid = (left + right) // 2
    ans = check(mid, n, k, a)

    if ans:
        right = mid 
    else:
        left = mid + 1

print(left)

