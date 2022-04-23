'''
주사위 굴리기2

크기가 nxm

1. 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한칸 굴러간다.
2. 주사위가 도착한 칸(x,y) 에 대한 점수를 획득한다.
3. 주사위의 아랫면에 있는 정수 a와 주사위가 있는 칸(x,y)에 있는 정수b를 비교해 이동 방향을 결정한다.
3-1. A>B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
3-2. A<B인 경우 이동 방향을 반시계방향으로 회전시킨다.
3-3. A=B인 경우 이동 방향에 변화 없다.
칸(x,y)에 대한 점수는 다음과 같이 구할 수 있다. (x,y)에 있는 정수를 B라고 했을 때, (x,y)에서 동서남북
방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다. 
<<이 때 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다.>>여기서 점수는 B와 C를 곱한 값이다.
def roll_dice(direction)
def get_score(r,c,number)
def get_direction()
'''
import copy
import pdb
from collections import deque
from random import vonmisesvariate
def get_score(r,c,number):
    global dr, dc,n,m,board
    cnt = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([r,c])
    visited[r][c]=True
    cnt+=1
    while q:
        cr,cc = q.popleft()
        # print(cr,cc)
        # pdb.set_trace()
        # if board[cr][cc]==number and visited[cr][cc]==False:
        #     visited[cr][cc]=True
        #     cnt+=1
        for d in range(4):
            nr = cr+dr[d]
            nc = cc+dc[d]
            if 0<=nr<n and 0<=nc<m and board[nr][nc]==number and visited[nr][nc]==False:
                q.append([nr,nc])
                visited[nr][nc]=True
                cnt+=1
    return cnt*number


    
def roll_dice(d):
    global dice
    n_dice = copy.deepcopy(dice)
    if d == 0:# 동
        n_dice[0] = dice[3]
        n_dice[2] = dice[0]
        n_dice[3] = dice[5]
        n_dice[5] = dice[2]
    if d == 1: # 남
        n_dice[0] = dice[1]
        n_dice[1] = dice[5]
        n_dice[4] = dice[0]
        n_dice[5] = dice[4]
    if d == 2: # 서
        n_dice[0] = dice[2]
        n_dice[2] = dice[5]
        n_dice[3] = dice[0]
        n_dice[5] = dice[3]
    if d == 3: # 북
        n_dice[0] = dice[4]
        n_dice[1] = dice[0]
        n_dice[4] = dice[5]
        n_dice[5] = dice[1]
    dice = n_dice
def get_next_direction(a,b):
    global d,r,c,dr,dc,n,m
    if a>b:
        d = (d+1)%4
    elif a<b:
        d = (d+3)%4
    nr = r+dr[d]
    nc = c+dc[d]
    if 0<=nr<n and 0<=nc<m:
        return
    else:
        d = (d+2)%4
    
n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dice = [1,2,3,4,5,6]
d = 0
dr = [0,1,0,-1] #동 남 서 북
dc = [1,0,-1,0]
r = 0
c = 0
ans=0
for _ in range(k):
    r = r+dr[d]
    c = c+dc[d]
    # print("r,c,d",r,c,d)
    roll_dice(d)
    ans += get_score(r,c,board[r][c])
    # print("score",get_score(r,c,board[r][c]))
    # print(dice[5],board[r][c])
    # print("dice",dice)
    get_next_direction(dice[5],board[r][c])
    # print()
print(ans)
