'''
start 2:18
블리자드 마법을 시전하려면 방향과 거리를 정해야한다.
1. d방향으로 거리가 s이하인 모든 칸에 얼음 파편을 던져 모두 파괴시킨다.
2. 구슬의 빈칸을 이동시킨다.
3. 구슬을 폭발시킨다
3-1. 4개 이상 연속하는 구슬이 있을대 폭발시킨다.
3-2. 구슬의 빈칸을 이동시킨다.
4. 그룹으로 바꾸고, 개수, 번호로 순서대로 쓴다.
def board_to_list():
def list_to_board():
def explode_balls():
    explod_balls_list = get_ball_list
def 
'''
import enum
import pdb
from collections import deque
def print_board(b):
    for l in b:
        print(l)
    print("="*10)
def destroy_balls(d,s):
    global board,n,dr,dc
    r,c = n//2,n//2
    # print_board(board)
    for i in range(1,s+1):
        nr = r+i*dr[d]
        nc = c+i*dc[d]
        board[nr][nc]=0
    # print_board(board)
def board_to_list(b):
    global n
    # 좌 하 우 상 => 2,1,3,0
    ball_list =[]
    dir_l = [2,1,3,0]
    r,c = n//2,n//2
    q = deque()
    q.append([r,c,1,0])
    cnt = 0
    num_change_dir = 0
    length = 1

    while q:
        cr,cc, c_cnt,d = q.popleft()
        # pdb.set_trace()
        nr = cr+dr[dir_l[d]]
        nc = cc+dc[dir_l[d]]
        n_cnt = c_cnt+1
        if nr>=0 and nc >=0 :
            if board[nr][nc]>0:
                ball_list.append(board[nr][nc])
                # print(nr,nc)
            if n_cnt<length:
                q.append([nr,nc,n_cnt,d])
            else:
                if num_change_dir==1:
                    length +=1
                    num_change_dir=0
                else:
                    num_change_dir+=1
                q.append([nr,nc,0,(d+1)%4])
    return ball_list

def explode_balls():
    global l
    def add_score(ball_list):
        global n_ball
        for number in [1,2,3]:
            n_ball[number] += len(ball_list[number])
            
    def get_explode_ball_list(l):
        from collections import defaultdict
        explode_ball_list = defaultdict(list)
        number = 0
        cnt = 0
        for i, ball in enumerate(l):
            if ball == number:
                cnt+=1
            else:
                if cnt>=4:
                    explode_ball_list[number]= explode_ball_list[number]+list(range(i-cnt+1,i+1))
                number = ball
                cnt = 1
        return explode_ball_list
    def delete_balls(explode_ball_list):
        global l
        total_delete_l = explode_ball_list[1]+explode_ball_list[2]+explode_ball_list[3]
        total_delete_l.sort()
        new_l = []
        for i, e in enumerate(l):
            if i+1 not in total_delete_l:
                new_l.append(e)
        l = new_l
    while True:
        # print("l",l)
        explode_ball_list = get_explode_ball_list(l)
        if len(explode_ball_list[1])==0 and len(explode_ball_list[2])==0 and len(explode_ball_list[3])==0:
            break
        # print(explode_ball_list)
        add_score(explode_ball_list)
        # pdb.set_trace()
        delete_balls(explode_ball_list)

def get_new_list(l):
    new_l = []
    number = 0
    cnt = 0
    for i, ball in enumerate(l):
        if ball == number:
            cnt+=1
        else:
            if number >0:
                new_l.append(cnt)
                new_l.append(number)
            number = ball
            cnt = 1
        if i == len(l)-1:
            new_l.append(cnt)
            new_l.append(number)
    return new_l
def list_to_board(l):
    global n
    r, c = n//2, n//2
    # 좌 하 우 상 => 2,1,3,0
    dir_l = [2,1,3,0]
    num_change_dir = 0
    length = 1
    cnt = 0
    d = 0
    b = [[0 for _ in range(n)] for _ in range(n)]
    for i, e in enumerate(l):
        
        if cnt >=length:
            if num_change_dir==1:
                length +=1
                num_change_dir =0
            else:
                num_change_dir+=1
            cnt =0
            d = (d+1)%4
        cnt+=1
        r = r+dr[dir_l[d]]
        c = c+dc[dir_l[d]]
        if r>=0 and c>=0:
            # print("rmc",r,c)
            b[r][c]=e
        else:
            break

    # pdb.set_trace()
    return b


        

dr = [-1,1,0,0]
dc = [0,0,-1,1]
n_ball= [0,0,0,0]
n,m=map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
for _ in range(m):
    d,s = map(int,input().split())
    destroy_balls(d-1,s)
    l = board_to_list(board)
    explode_balls()
    l = get_new_list(l)
    # print(l)
    board = list_to_board(l)
# print(n_ball)
print(n_ball[1]+2*n_ball[2]+3*n_ball[3])