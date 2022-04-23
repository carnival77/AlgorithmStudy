'''
마법사 상어와 복제

격자에는 물고기 m마리가 있다. 각 물고기는 격자의 칸 하나에 들어가 있으며, 이동 방향을 가지고 있다.
마법사 상어도 연습을 위해 격자에 들어가있다. 상어도 격자의 한 칸에 들어가있다. 둘이상의 물고기가
같은 칸에 있을 수 있으며, 마법사 상어와 물고기가 같은 칸에 있을 수도 있다.
마법 연습 한 번은 다음과 같은 작업이 순차적으로 이루어진다.
1. 상어가 모든 물고기에게 복제 마법을 시전한다. 복제 마법은 시간이 조금 걸리기 때문에, 5번에서 
물고기가 복제되어 칸에 나타난다.
2. 모든 물고기가 한 칸 이동한다. 1)상어가 있는 칸, 2)물고기의 냄새가 있는 칸, 3)격자의 범위를 벗어나는 칸으로
는 이동할 수 없다.각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도
반시계 회전시킨다. 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동한다.

3. 상어가 연속해서 3칸 이동한다. 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다. 연속해서
이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다. 연속해서 이동하는
중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면, 그 칸에 있는 모든 물고기는 격자에서 제외되며,
제외되는 모든 물고기는 물고기 냄새를 남긴다. 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법
으로 이동하며, 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다.

4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖는다.
사전순
상은 1, 좌는 2, 하는 3, 우는 4로 변환, 수를 이어 붙여 정수로 하나 만든다. a<b 만족하면 A가 B보다 사전순으로 앞선 것
def save_copy()
def move_fishes()
def move_shark():
def remove_past_smell()
def put_saved_fish()

'''
import copy
import pdb
def move_fishes():
    global fishes, smell, past_smell, shark,dr,dc
    t_smell = [[False for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if past_smell[i][j]==True or smell[i][j]==True:
                t_smell[i][j]=True
    for i,fish in enumerate(fishes):
        r,c,d = fish
        cnt =0
        while cnt<8:
            nr = r+dr[(d-cnt+8)%8]
            nc = c+dc[(d-cnt+8)%8]
            if 0<=nr<4 and 0<=nc<4 and not(nr==shark[0] and nc==shark[1]) and t_smell[nr][nc]==False:
                fishes[i]=[nr,nc,(d-cnt+8)%8]
                break
            else:
                cnt+=1
        
def remove_fish(l):
    global fishes, smell, past_smell
    past_smell = copy.deepcopy(smell)
    smell = [[False for _ in range(4)] for _ in range(4)]
    l.sort()
    new_fishes = []
    j = 0
    i=0
    while i<len(fishes) and j<len(l):
        # pdb.set_trace()
        if i == l[j]-j:
            j+=1
            del fishes[i]
        else:
            i+=1
        
    # for i, fish in enumerate(fishes):
    #     if i not in l:
    #         new_fishes.append(fish)
    #     else:
    #         r,c,_ = fish
    #         smell[r][c]=True
    # fishes = new_fishes           
def move_shark(cnt, c_list_fish, n_shark, route):
    # TODO: 상어가 한 방향으로만 가지 않고, 가다게ㅏ 꺾을 수 있다.
    # 방향은 매번 상하좌우 중 하나를 고를 수 있다. => DFS 알고리즘으로 찾으면 될것같음.
    global smell, fishes, board_fish, max_fish, list_fish, shark, visited
    dr = [-1,0,0,1]
    dc = [0,-1,1,0]
    if cnt == 3:
        if max_fish<len(c_list_fish):
            max_fish = len(c_list_fish)
            list_fish = c_list_fish
            shark = n_shark
            return
    else:
        for d in range(4):
            n_route = route+str(d)
            if n_route not in routes :
                nr = n_shark[0]+dr[d]
                nc = n_shark[1]+dc[d]
                
                if 0<=nr<4 and 0<=nc<4 and visited[nr][nc]==False:
                    routes.append(n_route)
                    n_cnt = cnt+1
                    n_fish_list= c_list_fish+board_fish[nr][nc]
                    visited[nr][nc]=True
                    move_shark(n_cnt,n_fish_list,[nr,nc], n_route)
                    visited[nr][nc]=False
                    

    


            
def print_board(b):
    for l in b:
        print(l)
    print("="*10)


dr = [0,-1,-1,-1,0,1,1,1]
dc = [-1,-1,0,1,1,1,0,-1]
m,s = map(int,input().split())
fishes = [list(map(int,input().split())) for _ in range(m)]

for r, fish in enumerate(fishes):
    fishes[r][0] = fish[0]-1
    fishes[r][1] = fish[1]-1
    fishes[r][2] = fish[2]-1
    # print(fish[1]-1)
shark = list(map(int,input().split()))
shark[0] = shark[0]-1
shark[1] = shark[1]-1
smell = [[False for _ in range(4)] for _ in range(4)]
past_smell = [[False for _ in range(4)] for _ in range(4)]
for _ in range(s):
    saved_fishes = copy.deepcopy(fishes)
    # print("saved fish", fishes)
    # pdb.set_trace()
    move_fishes()
    # print("after moving", fishes)
    max_fish = 0
    board_fish = [[[] for _ in range(4)] for _ in range(4)]
    for i,fish in enumerate(fishes):
        r,c,_ = fish
        board_fish[r][c].append(i)
    list_fish = []
    routes = []
    visited = [[False for _ in range(4)] for _ in range(4)]
    move_shark(0,[],copy.deepcopy(shark),"")
    remove_fish(list_fish)
    # print_board(past_smell)
    # print("after eataing fish",fishes)
    fishes = fishes + saved_fishes
    # print("after adding fish", fishes)
    # print("shark", shark)
print(len(fishes))