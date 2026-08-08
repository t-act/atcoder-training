from functools import reduce
import operator

n, q = map(int, input().split())
a = [0]*n

queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

x = 0 # 全体のXOR

for query in queries: #O(q)
    if query[0] == 1:
        a[query[1]-1] += 1
    else:
        for i in range(len(a)): #O(n)←これをへらす
            if a[i] >= 1:
                a[i] -= 1
    # 配列のすべての要素に対して排他的論理和を計算O(n)←これを減らす
    total_xor = reduce(operator.xor, a)
    print(total_xor)
