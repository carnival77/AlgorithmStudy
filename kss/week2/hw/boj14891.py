'''
톱니바퀴
1. 톱니바퀴 회전
1.1. 12시 방향이 0이다.
2. 점수를 계산한다.
def rotate_gears(n, d):
    rotating_gears = get_rotating_gears(n,d)
    # rotating gears 에 들어가야하는 것: gear index, 회전 방향
    for gear in rotating_gears:
        cn, cd = gear
        gears[cn].rotate(cd)
def get_score(gears):
    ans=0
    for i,gear in enumerate(gears):
        ans+=gear<<i
    return ans
'''
from collections import deque

import pdb

def print_gears(gears):
    for gear in gears:
        print(gear)
    print("="*10)
def get_score(gears):
    ans = int(gears[0][0]<<0) + int(gears[1][0]<<1)+int(gears[2][0]<<2)+int(gears[3][0]<<3)
    # pdb.set_trace()
    # for i, gear in enumerate(gears):
        # pdb.set_trace()
        # ans = ans+ gear[0]<<i
        # print(ans)
    return ans
def get_rotating_gears(n,d):
    # 오른쪽
    # gears[n][2] == gears[n+1][2=6]
    # 왼쪽
    # gears[n][6] == gears[n-1][2]
    global gears
    rotating_gears = [[n,d]]
    q = deque()# 방향, index
    for dd in [-1,1]:
        nn = n+dd
        if 0<=nn<4:
            q.append([nn,-1*d, dd])
    while q:
        cn, cd, rl = q.popleft()
        if rl == 1 and gears[cn-1][2]!=gears[cn][6]:
            rotating_gears.append([cn, cd])
            nn = cn+rl
            if 0<=nn<4:
                q.append([nn,-1*cd, rl])
            
        elif rl == -1 and gears[cn+1][6]!=gears[cn][2]:
            rotating_gears.append([cn, cd])
            nn = cn+rl
            if 0<=nn<4:
                q.append([nn,-1*cd, rl])
        
    return rotating_gears



def rotate_gears(n,d):
    global gears
    rotating_gears = get_rotating_gears(n-1,d)
    # print("rotating gears", rotating_gears)
    for gear in rotating_gears:
        cn,cd = gear
        # print("here",cn,cd)
        gears[cn].rotate(cd)

gears_l = [str(input()) for _ in range(4)]
gears = []
for g in gears_l:
    q = deque()
    for c in list(g):
        i = int(c)
        q.append(i)
    gears.append(q)
# print(gears)
k = int(input())
for _ in range(k):
    n,d = map(int,input().split())
    # print("before rotating gear")
    rotate_gears(n,d)
print(get_score(gears))