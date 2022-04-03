'''
1. 모든 파이어볼은 d의 방향으로 s만큼 이동한다.(같은 칸에 여러 개의 파이어볼이 있을 수 있다.)
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
1) 1개로 합쳐지고, 4개로 나누어진다.
2) 질량 =  (질량합)//5, 속력=(속력합)//(개수), 방향이 모두 홀수/짝수면 0,2,4,6 방향되고, 아니면 1,3,5,7
질량이 0인 파이어볼은 소멸되어 없어진다.
k번 명령한 후 남아있는 파이어볼의 질량의 합을 구해보자

'''


def sum_mass(balls):
    s = 0
    for ball in balls:
        mass = ball[2]
        s+=mass
    return s
def move_fireballs():
    global fireballs,dr,dc
    new_fireballs = []
    for i,fireball in enumerate(fireballs):
        r,c,m,s,d = fireball
        nr = (n+r+dr[d]*s)%n
        nc = (n+c+dc[d]*s)%n
        fireballs[i][0], fireballs[i][1] = nr,nc
def get_fireball_board():
    global fireballs,n
    board = [[[] for _ in range(n)] for _ in range(n)]
    for fireball in fireballs:
        r,c,m,s,d = fireball
        board[r][c].append([m,s,d])
    return board
def get_new_parameters(l):
    nm,ns,nd_list = 0,0,[]
    sm,ss=0,0
    num_odd, num_even = 0,0
    for m,s,d in l:
        sm +=m
        ss+=s
        if d%2 ==0:
            num_even+=1
        else:
            num_odd+=1
    nm = sm//5
    ns = ss//len(l)
    if num_odd ==len(l) or num_odd == 0:
        nd_list = [0,2,4,6]
    else:
        nd_list = [1,3,5,7]
    return nm,ns,nd_list

def get_new_fireballs(b):
    new_fireballs = []
    for r,l in enumerate(b):
        for c,ball_list in enumerate(l):
            if len(ball_list)>1:
                nm,ns,nd_list= get_new_parameters(ball_list)
                if nm>0:
                    for nd in nd_list:
                        fireball = [r,c]+[nm,ns,nd]
                        new_fireballs.append(fireball)

            elif len(ball_list)==1:
                fireball = [r,c]+ball_list[0]
                new_fireballs.append(fireball)
    return new_fireballs
                

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]
n,m,k = map(int,input().split())
fireballs = [list(map(int,input().split())) for _ in range(m)]
for _ in range(k):
    move_fireballs()
    fireball_board = get_fireball_board()
    fireballs = get_new_fireballs(fireball_board)
print(sum_mass(fireballs))
