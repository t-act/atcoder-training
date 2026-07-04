# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 要素数をn個に合わせるために先頭に0を挿入
a = [0] + a
b = [0,0] + b

time_dict = {1: 0, 2: a[1]}  # room1 -> room2 の所要時間はA2=a[1]
room_counter = 3  # room1, room2までは確定 -> room3からスタート

# 最後の部屋に到達するまで繰り返す
for i in range(3,n+1):
    # 部屋kからnまでの所要時間はどちらのほうがお得か
    a_time = a[i-1] + time_dict[i-1]
    b_time = b[i-1] + time_dict[i-2]
    if b_time <= a_time:
        time_dict[i] = b_time
    else:
        time_dict[i] = a_time
    # print(f"room_counter: {i}, time_dict: {time_dict}")

print(time_dict[n])