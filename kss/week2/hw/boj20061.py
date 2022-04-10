# boj 20061 모노미노도미노 2
"""
시작: 1:24 끝:3:00
1) 빨간색 보드, 파란색 보드, 초록색 보드가 그림과 같이 붙어있다. 게임에서 사용하는 좌표 (x,y)에서 x는 행, y는 열을 의미한다. 빨간색, 파란색, 초록색 보드가 사용하는 좌표는 그 색으로 그림에 적혀있다. 
2) 빨간색 보드에 있는 블록을 파란 보드, 초록 보드 쪽으로 각각 끝까지 보낸다
3) 모든 열이 다 찬 행이 없을 때 까지 다 찬 행이 있는지 확인한다.
4) 해당 행이 존재하면 그 행을 없앤다. 점수를 1 올린다.
5) 지운 행 위의 모든 블록들을 밑으로 내린다.
6) 연한 칸에 블록이 존재하면 맨 아랫 칸을 지우고, 모든 블록을 한칸씩 내린다.
7) 모든 게임이 끝났을 때 얻은 점수와 파랑, 초록 보드에 타일이 들어있는 칸의 개수를 출력한다.
"""
from collections import deque
import pdb
def put_block(board, t,r,c,b_flag):
    block_loc = []
    
    if b_flag == 0:
        board[r][c] = 1
        block_loc.append([r,c])
        if t == 2:
            board[r][c+1] =1
            block_loc.append([r,c+1])
        elif t == 3:
            board[r+1][c] = 1
            block_loc.append([r+1,c])
        return block_loc
    else:
        nr = c
        nc = 3-r
        board[nr][nc]=1
        block_loc.append([nr,nc])
        if t == 2:
            board[nr+1][nc] =1
            block_loc.append([nr+1,nc])
        elif t == 3:
            board[nr][nc-1] = 1
            block_loc.append([nr,nc-1])
        return block_loc


def drop_block(board,block_loc,t):
    # pdb.set_trace()
    moving_rows = 0
    block_loc = sorted(block_loc,key=lambda x:x[0],reverse=True)
    for i in range(1,10):
        flag = True
        if t == 2:
            for c_block in block_loc:
                cr,cc = c_block
                nr = cr+i
                nc = cc
                if nr>=10 or board[nr][nc]!=0:
                    flag = False
                    break
        else:
            cr,cc = block_loc[0]
            nr = cr+i
            nc = cc
            if nr>=10 or board[nr][nc]!=0:
                flag = False
                break
        if flag:
            moving_rows =i
        else:
            break
    for block in block_loc:
        cr,cc = block
        nr = cr+moving_rows
        board[cr][cc]=0
        board[nr][cc]=1
    


def get_full_line(board):
    l = []
    for r in range(9,3,-1):
        is_full = True
        for c in range(4): 
            # pdb.set_trace()
            if board[r][c]==0:
                is_full = False
                break
        if is_full:
            l.append(r)
    return l
def remove_line(board, r):
    for c in range(4):
        board[r][c]=0

def drop_line(board, r):
    for cr in range(r,3,-1):
        for c in range(4):
            board[cr][c] = board[cr-1][c]

def get_blocks_in_light(board):
    for r in range(4,6):
        for c in range(4):
            if board[r][c]==1:
                if r == 4:
                    return 2
                elif r == 5:
                    return 1
    return 0
def count_blocks(board):
    a = 0
    for r in range(4,10):
        for c in range(4):
            if board[r][c]==1:
                a+=1
    return a
g_board = [[0 for _ in range(4)] for _ in range(10)]
b_board = [[0 for _ in range(4)] for _ in range(10)]
n = int(input())
score = 0
for i in range(n):
    t,r,c = map(int,input().split())
    g_block_loc = put_block(g_board,t,r,c,0)
    b_block_loc = put_block(b_board,t,r,c,1)
    drop_block(g_board,g_block_loc, t)
    n_t = t
    if t == 2:
        n_t = 3
    elif t == 3:
        n_t = 2
    drop_block(b_board,b_block_loc,n_t)
    # print("after dropping blocks")
    # print("g board")
    # for r in range(10):
    #     print(g_board[r])
    # print("b borad")
    # for r in range(10):
    #     print(b_board[r])
    g_full_lines = get_full_line(g_board)
    b_full_lines = get_full_line(b_board)
    for idx, line in enumerate(g_full_lines):
        remove_line(g_board,line+idx)
        drop_line(g_board,line+idx)
        score+=1
    for idx,line in enumerate(b_full_lines):
        remove_line(b_board,line+idx)
        drop_line(b_board,line+idx)
        score+=1
    # print("after removing lines")
    # print("g board")
    # for r in range(10):
    #     print(g_board[r])
    # print("b borad")
    # for r in range(10):
    #     print(b_board[r])
    g_light_blocks = get_blocks_in_light(g_board)
    for i in range(g_light_blocks):
        remove_line(g_board,9)
        drop_line(g_board,9)
    b_light_blocks = get_blocks_in_light(b_board)
    for i in range(b_light_blocks):
        remove_line(b_board,9)
        drop_line(b_board,9)
    # print("after removing light parts")
    # print("g board")
    # for r in range(10):
    #     print(g_board[r])
    # print("b borad")
    # for r in range(10):
    #     print(b_board[r])
print(score)
num_blocks = 0
num_blocks += count_blocks(g_board)
num_blocks += count_blocks(b_board)
for r in range(4):
    for c in range(4):
        num_blocks+=g_board[r][c]
print(num_blocks)