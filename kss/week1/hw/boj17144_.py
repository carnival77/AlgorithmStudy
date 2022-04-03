'''
boj 17144 미세먼지 안녕!
1초동안 아래 적힌 일이 순서대로 일어난다.
1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
1-1. r,c에 있는 미세먼지는 인접한 네 방향으로 확산된다.
1-2. 확산되는 양은 Arc/5이며 소수점은 버린다.
1-3. r,c에 남은 미세먼지의 양은 Arc-(Arc/5)*확산된 방향의 개수
2. 공기청정기가 작동한다.
2-1. 공기청정기에서는 바람이 나온다.
2-2. 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
2-3. 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
2-4. 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
spread_dust()
모든 r, c에 대해서 difference matrix를 만들어서 다 넣은 후 마지막에 원래 matrix와 더한다.
clean_air(air_cleaner_location)
upper_circle()
move_right(starting_point, ending_point)
move_left()
move_up()
move_down()
위의 공기를 1칸씩 옮긴다.
lower_circle()
아래 공기를 1칸씩 옮긴다.
'''
import pdb
def get_all_dust(b):
    s = 0
    for l in b:
        for e in l:
            if e>0:
                s+=e
    return s
def print_board(b):
    for l in b:
        print(l)
    
def spread_dust():
    global R,C,board, air_cleaner_row_idx
    diff_board = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c]>0:
                cnt = 0
                for d in range(4):
                    nr = r+dr[d]
                    nc = c+dc[d]
                    # pdb.set_trace()
                    if 0<=nr<R and 0<=nc<C and board[nr][nc]!=-1:
                        diff_board[nr][nc] += board[r][c]//5
                        cnt+=1
                diff_board[r][c]-= (board[r][c]//5)*cnt
    # pdb.set_trace()
    for r in range(R):
        for c in range(C):
            board[r][c] += diff_board[r][c]
    
def clean_air():
    global air_cleaner_row_idx
    clean_upper_circle(air_cleaner_row_idx[0])
    clean_lower_circle(air_cleaner_row_idx[1])
from collections import deque
def clean_upper_circle(sr):
    global board
    q = deque()
    cur_dust = board[sr][1]
    q.append([sr,2])
    dd = [0,3,1,2]
    d = 0
    board[sr][1]=0
    while q:
        cr,cc = q.popleft()
        # print("cur loc ",cr,cc)
        #1. 먼저 저장, 후 업데이트
        cv = board[cr][cc]
        
        if not (cr==sr and cc ==0):
            board[cr][cc]=cur_dust
            cur_dust = cv
            nr=cr+dr[dd[d]]
            nc=cc+dc[dd[d]]
            # print("first next loc",nr,nc)
            if 0<=nr<R and 0<=nc<C:
                q.append([nr,nc])
            else:
                d = d+1
                nd = dd[d]
                # print("change direction")
                # print(d,dd)
                # print("next direction : ",nd)
                # pdb.set_trace()
                nr=cr+dr[dd[d]]
                nc=cc+dc[dd[d]]
                q.append([nr,nc])
        else:
            break
def clean_lower_circle(sr):
    global board
    q = deque()
    cur_dust = board[sr][1]
    q.append([sr,2])
    dd = [0,2,1,3]
    board[sr][1]=0
    d = 0
    while q:
        cr,cc = q.popleft()
        #1. 먼저 저장, 후 업데이트
        cv = board[cr][cc]
        if not(cr==sr and cc ==0):
            board[cr][cc]=cur_dust
            cur_dust = cv
            nr=cr+dr[dd[d]]
            nc=cc+dc[dd[d]]
            if 0<=nr<R and 0<=nc<C:
                q.append([nr,nc])
            else:
                d = d+1
                nr=cr+dr[dd[d]]
                nc=cc+dc[dd[d]]
                q.append([nr,nc])
        else:
            break
R,C,T = map(int,input().split())
dr = [0,0,1,-1] # 우 좌 하 상
dc = [1,-1,0,0]
board = [list(map(int,input().split())) for _ in range(R)]
air_cleaner_row_idx = [0,0]
for r in range(R):
    if board[r][0]==-1:
        air_cleaner_row_idx = [r,r+1]
        break
for _ in range(T):
    spread_dust()
    clean_air()
print(get_all_dust(board))