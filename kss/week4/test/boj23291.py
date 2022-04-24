import enum
import pdb
import copy
def add_fish():
    global tanks
    min_fish = min(tanks)
    for i, fish in enumerate(tanks):
        if fish == min_fish:
            tanks[i]+=1
def print_board(b):
    for l in b:
        print(l)
    print("="*10)
def rotate_and_stack(r, cnt):
    # if cnt == 1: 90도, if cnt == 2: 180도
    global tanks
    for _ in range(cnt):
        a,b= tanks[:r], tanks[r:]
        na = [[ 0 for _ in range(r)] for _ in range(len(a[0]))]
        for rr, l in enumerate(a):
            for cc, num in enumerate(l):
                na[cc][r-rr-1]=num

        print_board(a)
        print_board(na)
        n
        for rr in range(len(na)):
            # b.append([0 for _ in range(b[0])])
            for cc in range(len(na[0])):
                b[rr].append(na[rr][cc])
        print_board(b)
        tanks = b
n,k = map(int,input().split())
tanks = list(map(int,input().split()))
def to_list(t):
    l_t = copy.deepcopy(t)
    for i,tank in enumerate(t):
        l_t[i]=[tank]
    return l_t
def to_num(t):
    n_t = copy.deepcopy(t)
    for i,tank in enumerate(t):
        n_t[i]=tank[0]
    return n_t
# TODO : MOVE FISHES METHOD NEED TO BE DONE
def move_fishes():
    global tanks
    dr = [0,1,0,-1] # 오 왼 아래 위
    dc = [1,0,-1,0]
    C = len(tanks)
    R = 0
    for c, tank_l in enumerate(tanks):
        if len(tank_l)>R:
            R = len(tank_l)
    t_board = [[0 for _ in range(C)] for _ in range(R)]
    d_board = [[0 for _ in range(C)] for _ in range(R)]
    v_board = [[[False,False,False,False] for _ in range(C)] for _ in range(R)]
    for c, tank_l in enumerate(tanks):
        for r, tank in enumerate(tank_l):
            t_board[r][c] = tank
    for r, l in enumerate(t_board):
        for c, t in enumerate(l):
            if t_board[r][c]>0:
                for d in range(4):
                    # pdb.set_trace()
                    # TODO: VISITED Not working....
                    nr = r+dr[d]
                    nc = c+dc[d]
                    if 0<=nr<R and 0<=nc<C and t_board[nr][nc]>0 and v_board[r][c][d] ==False and abs(t_board[r][c]-t_board[nr][nc])>=5:
                        diff = abs(t_board[r][c]-t_board[nr][nc])//5
                        v_board[r][c][d] = True
                        v_board[nr][nc][(d+2)%2]=True
                        if min(t_board[r][c],t_board[nr][nc])==t_board[r][c]:# r,c 더 작을때
                            d_board[r][c]+=diff
                            d_board[nr][nc]-=diff
                        else:
                            d_board[r][c]-=diff
                            d_board[nr][nc]+=diff
    for r, l in enumerate(t_board):
        for c, t in enumerate(l):
            t_board[r][c]+=d_board[r][c]
    
    print("t board")
    print_board(t_board)
    # pdb.set_trace()
    tanks = board_to_tanks(t_board)

t = 0
num_rotate = int(n**(1/2))*2
if n**(1/2) -int(n**(1/2))>0:
    num_rotate-=1

# num_rotate = get_rotate_num(n)
while True:
    if max(tanks)-min(tanks)<=k:
        print(t)
        exit()
    add_fish()
    tanks = to_list(tanks)
    # rotate_and_stack(1,1)
    cnt = 0
    h = 1
    for _ in range(num_rotate):
        rotate_and_stack(h,1)
        cnt+=1
        if cnt == 2:
            cnt = 0
            h +=1
    # exit()
    move_fishes()
    # lineup_tank()
    # rotate_and_stack(n//2,2)
    # rotate_and_stack(n//4,2)
    # move_fishes()
    # lineup_tank()
    # tanks = to_num(tanks)

    
