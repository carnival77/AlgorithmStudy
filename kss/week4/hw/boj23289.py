from collections import deque
import pdb
def print_board(b):
    for l in b:
        print(l)
    print("="*10)
def get_check_locs(b):
    locs = []
    for r, l in enumerate(b):
        for c, e in enumerate(l):
            if e == 5:
                locs.append([r,c])
    return locs
def get_heaters(b):
    locs = []
    for r, l in enumerate(b):
        for c, e in enumerate(l):
            if 1 <= e < 5:
                locs.append([r,c,e-1])
    return locs
def get_wall_board(walls):
    global r,c
    b = [[[False,False] for _ in range(c+2)] for _ in range(r+2)]
    for wall in walls:
        x,y,t = wall
        b[x-1][y-1][t]=True
    return b
r,c,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(r)]
t_board = [[0 for _ in range(c)] for _ in range(r)]
check_locs = get_check_locs(board)
heaters = get_heaters(board)
w = int(input())
walls = []
w_board = [[[False]*4 for _ in range(c)] for _ in range(r)]
for _ in range(w):
    x,y,t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        w_board[x][y][2] = w_board[x-1][y][3] = True
    else:
        w_board[x][y][0] = w_board[x][y+1][1] = True
t = 0
dr = [0,0,-1,1]
dc = [1,-1,0,0]

def chill_edge():
    global t_board,r,c
    # 위 (0,[0-c])
    for i in range(c):
        if t_board[0][i]>0:
            t_board[0][i]-=1
    # 아래 (r-1,[0-c])
    for i in range(c):
        if t_board[r-1][i]>0:
            t_board[r-1][i]-=1
    # 왼 ([0-r],0)
    for i in range(r):
        if t_board[i][0]>0:
            t_board[i][0]-=1
    # 오 ([0-r],c-1)
    for i in range(r):
        if t_board[i][c-1]>0:
            t_board[i][c-1]-=1
    t_board[0][0]+=1
    t_board[0][c-1]+=1
    t_board[r-1][0]+=1
    t_board[r-1][c-1]+=1
    
def is_done():
    global t_board, check_locs,k
    for r,c in check_locs:
        if t_board[r][c]<k:
            return False
    return True
def is_blocked(r,c,d):
    global w_board
    # pdb.set_trace()
    if w_board[r][c][d]:
        return True
    return False

def blow_heater():# bfs로 풀어야함.
    global t_board, board,heaters, walls,r,c
    change_dir = {0:[2,3],1:[2,3],2:[1,0],3:[1,0]}
    d_board = [[0 for _ in range(c)] for _ in range(r)]
    for heater in heaters:
        rr,cc,d = heater
        visited = [[False for _ in range(c)] for _ in range(r)]
        q = deque()
        nr = rr+dr[d]
        nc = cc+dc[d]
        q.append([nr,nc,d,5,0])
        print("heater",heater)
        print("before heater")
        print_board(d_board)
        while q:
            # pdb.set_trace()
            cr,cc,cd, cn,is_edge = q.popleft()
            d_board[cr][cc] += cn
            nr = cr+dr[cd]
            nc = cc+dc[cd]
            nn = cn-1
            print(cr,cc,cd,cn)
            if cn == 3 and cc == 3:
                pdb.set_trace()
            # if cn == 5:
            #     if 0<=nr<r and 0<=nc<c and visited[nr][nc]==False and not is_blocked(cr,cc,cd):
            #         q.append([nr,nc,cd,nn,0])
            #         visited[nr][nc]=True
            #     for ni, nd in enumerate(change_dir[cd]):
            #         nnr = nr+dr[nd]
            #         nnc = nc+dc[nd]
            #         if 0<=nnr<r and 0<=nnc<c and visited[nnr][nnc]==False and not is_blocked(cr,cc,nd):
            #             q.append([nnr,nnc,cd,nn,ni+1])
            #             visited[nnr][nnc]=True
            # else:
            if nn>0:
                if 0<=nr<r and 0<=nc<c and visited[nr][nc]==False and not is_blocked(cr,cc,cd):
                    q.append([nr,nc,cd,nn,0])
                    visited[nr][nc]=True
                # if is_edge>0:
                    # nd = change_dir[cd][is_edge-1]
                    for nd in change_dir[cd]:
                        nnr = nr+dr[nd]
                        nnc = nc+dc[nd]
                        # pdb.set_trace()
                        # if nnr == 3 and nnc == 3:
                        #     pdb.set_trace()
                        if 0<=nnr<r and 0<=nnc<c and visited[nnr][nnc]==False and not (is_blocked(cr,cc,nd) and is_blocked(nnr-dr[cd],nnc-dc[cd],cd)):
                            q.append([nnr,nnc,cd,nn,is_edge])
                            visited[nnr][nnc]=True
        print("after heater")
        print_board(d_board)

    return d_board


def defuse_heat():
    global t_board, board,heaters, walls,r,c
    d_board = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            total_tmp = 0
            for d in range(4):
                nr = i+dr[d]
                nc = j+dc[d]
                if 0<=nr<r and 0<=nc<c and t_board[i][j]>t_board[nr][nc]:
                    if not is_blocked(i,j,d):
                        d_tmp = (t_board[i][j]-t_board[nr][nc])//4
                        d_board[nr][nc]+=d_tmp
                        total_tmp +=d_tmp
            d_board[i][j]-=total_tmp
                # pdb.set_trace()
    return d_board

def change_board(b):
    global t_board
    for r, l in enumerate(t_board):
        for c, e in enumerate(l):
            t_board[r][c] = e+b[r][c]


while True:
    d_board = blow_heater()
    print_board(d_board)
    change_board(d_board)
    d_board = defuse_heat()
    print("defuse diff board")
    print_board(d_board)
    print("before defusing")
    print_board(t_board)
    change_board(d_board)
    print("defuse t_board")
    print_board(t_board)
    chill_edge()
    print("after chill edge")
    print_board(t_board)
    t+=1
    if is_done():
        print(t)
        exit()
    elif t == 100:
        print(101)
    if t == 53:
        pdb.set_trace()

print(t)