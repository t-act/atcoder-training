import collections

n = int(input())
c = list(map(int, input().split()))

count = collections.Counter(c)
max_num = max(count.values())
print(n-max_num)