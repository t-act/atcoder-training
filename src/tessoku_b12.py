# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ck

def eq(x):
    return x**3 + x

def check_over(x, n):
    if eq(x) >= n:
        return True
    else:
        return False

n = int(input())

left, right = 0.0, 50.0  # (1 <= n< =1e5) なので 1e5**(1/3)~46
for _ in range(100):
    mid = (left + right) / 2
    if check_over(mid, n):
        right = mid
    else:
        left = mid

print(left)
