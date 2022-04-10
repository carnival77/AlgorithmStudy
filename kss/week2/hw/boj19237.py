#boj 19237 어른상어
"""
시작: 9:11 끝: 10:22
1) 자신의 위치에 자신의 냄새를 뿌린다.
2) 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다.
3) 냄새는 상어가 k번 이동하면 사라진다.
3) 상어가 이동방향을 결정할 때
3-1) 인접한 칸 중 아무 냄새가 없는 칸으로 방향을 잡는다.
3-2) 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
4) 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
"""
from collections import defaultdict
import heapq
import pdb
def get_destination(shark_idx, cur):
    global board,n,priority
    dr = [-1,1,0,0]# 0,1,2,3 
    dc= [0,0,-1,1]#상하좌우
    cr,cc,cd = cur
    is_blank = False
    candi = []
    # pdb.set_trace()
    # print(priority[shark_idx-1][cd])
    for d in priority[shark_idx-1][cd]:
        nr = cr+dr[d]
        nc = cc+dc[d]
        if 0<=nr<n and 0<=nc<n :
            if board[nr][nc][0]==0:
                is_blank=True
                return [nr,nc,d]
            elif board[nr][nc][0]==shark_idx:
                candi.append([nr,nc,d])
    if len(candi)>0:
        for d in priority[shark_idx-1][cd]:
            for c in candi:
                if c[2]==d:
                    nr = cr+dr[d]
                    nc = cc+dc[d]
                    return [nr,nc,d]
    
def remove_smell():
    global board, sharks,n
    for r in range(n):
        for c in range(n):
            if board[r][c][0]>0:
                if board[r][c][1]>1:
                    board[r][c][1]-=1
                else:
                    board[r][c] = [0,0]
def spread_smell():
    global sharks,board,k
    # pdb.set_trace()
    for s_i, shark in sharks.items():
        # smells.append([s_i,k])
        r,c,_ = shark
        board[r][c] = [s_i,k]

def kick_out_shark():
    global sharks
    same_loc = defaultdict(list)
    for s_i, shark in sharks.items():
        # pdb.set_trace()
        same_loc[tuple(shark[:2])].append(s_i)
    for loc, s_l in same_loc.items():
        if len(s_l)>1:
            s_l.sort()
            for i in range(1,len(s_l)):
                del sharks[s_l[i]]

n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
sharks = {}
# smells = 
for r in range(n):
    for c in range(n):
        if board[r][c]>0:
            sharks[board[r][c]] = [r,c]
            board[r][c] = [board[r][c],k]
        else:
            board[r][c] = [0,0]

directions = list(map(int,input().split()))
for i,d in enumerate(directions):
    sharks[i+1].append(d-1)
# print(sharks)
priority = [[list(map(int,input().split())) for _ in range(4)] for _ in range(len(sharks.keys()))]
for idx,shark in enumerate(priority):
    for d in range(4):
        for i in range(4):
            priority[idx][d][i] -=1
# print(priority)
t=0
while t<=1000:
    if len(sharks)==1:
        print(t)
        exit()
    # print("time ",t)
    # print("before moving", sharks)
    for s_i, shark in sharks.items():
        sharks[s_i] = get_destination(s_i,shark)
    # print("after moving",sharks)
    kick_out_shark()
    # print("after kickout", sharks)
    remove_smell()
    # print("after remove smell")
    # for r in range(n):
    #     print(board[r])
    spread_smell()
    # print("after spread smell")
    # for r in range(n):
    #     print(board[r])
    
    t+=1
print(-1)