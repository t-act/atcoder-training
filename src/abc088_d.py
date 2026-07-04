# https://atcoder.jp/contests/abc088/tasks/abc088_d

from collections import deque

h, w = map(int, input().split())
start = (0, 0)
goal = (h-1, w-1)

s = []
for rr in range(h):
    grid = list(input())
    s.append(grid)


def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])

    visited = {start}       # 訪問したかを記録
    que = deque([start])
    parent = {start: None}  # 各セルをどのセルから発見したかを記録(key: 移動後, value: 移動前)

    while que:
        r, c = que.popleft()

        # goalか確認
        if (r, c) == goal:
            path = []
            node = (r, c)
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]

        # 上下左右を確認を確認して進めるならばをqueueにpush
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r+dr, c+dc  # 移動後
            if (0 <= nr < rows and 0<= nc < cols   # grid範囲内か
                    and maze[nr][nc] != "#"         # 壁でないか
                    and (nr, nc) not in visited):   # 未訪問か
                # 発見したらvisitedに登録する
                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)  # key: 移動後, value: 移動前
                que.append((nr, nc))
    return -1

total_cells = h * w

total_black_cells = 0
for row in s:
    for cell in row:
        if cell == "#":
            total_black_cells += 1

try:
    move_cells = len(bfs(s, start, goal))
    ans = total_cells - move_cells - total_black_cells
    print(ans)
except:
    print(-1)

