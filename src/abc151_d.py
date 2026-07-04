# https://atcoder.jp/contests/abc151/tasks/abc151_d
from collections import deque

def bfs(maze, start):
    rows, cols = len(maze), len(maze[0])
    que = deque([start])
    dist = {start: 0}

    while que:
        r, c = que.popleft()
        for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
            nr, nc = dr+r, dc+c
            if (0 <= nr < rows and 0 <= nc < cols 
                    and (nr, nc) not in dist
                    and maze[nr][nc] != "#"):
                que.append((nr, nc))
                dist[(nr, nc)] = dist[(r,c)] + 1
    return max(dist.values())
        


h, w = map(int, input().split())

s = []
for rr in range(h):
    grid = list(input())
    s.append(grid)

ans = 0

for i, row in enumerate(s):
    for j, cell in enumerate(row):
        if cell == ".":
            move_count = bfs(s, (i, j))
            ans = max(ans, move_count)

print(ans)