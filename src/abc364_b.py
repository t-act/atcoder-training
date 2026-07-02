# https://atcoder.jp/contests/abc364/tasks/abc364_b
import copy

# input
h, w = map(int, input().split())
s_i, s_j = map(int, input().split())
s = [s_i, s_j]

c = []

for i in range(h):
    c_j = input()
    c.append(list(c_j))

x = list(input())


# method
def move_action(x: str, p: list[int,int]) -> list[int,int]:
    new_p = copy.deepcopy(p)
    if x == "L":
        new_p[1] -= 1
    elif x == "R":
        new_p[1] += 1
    elif x == "U":
        new_p[0] -= 1
    elif x == "D":
        new_p[0] += 1
    return new_p

def judge_move(c: list[str,str], new_position_idx: list[int,int]) -> bool:
    """
    new_position(移動後のインデックス)を受け取り、. or # を判定
    . -> True
    # -> False
    を返す
    """
    new_i, new_j = new_position_idx[0], new_position_idx[1]
    if 0 < new_i <= h and 0 < new_j <= w:
        if c[new_i-1][new_j-1]  == ".":
            return True
        else:
            return False
    else:
        return False

for act in x:
    new_position_idx = move_action(act, s)
    if judge_move(c, new_position_idx):
        new_s = [new_position_idx[0], new_position_idx[1]]
        s = new_s

print(*s)