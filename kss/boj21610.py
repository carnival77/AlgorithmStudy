'''
비바라기를 시전하면(N,1),(N,2),(N-1,1),(M-1,2) 에 비구름이 생긴다.
구름은 칸 전체를 차지한다.
구름에 이동을 M번 명령한다.
이동을 명령하면 다음이 실행된다.
1. 모든 구름이 d방향으로 s칸 이동
2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
3. 구름이 모두 사라진다.
4. 2에서 물이 증가한 칸(r,c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로
거리가 1인 칸에 물이 있는 바구니의 수만큼(r,c)에 있는 바구니의 물이 양이 증가한다.
4-1. 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
4-2. 예
5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는
칸은 3에서 구름이 사라진 칸이 아니어야한다.

'''
import pdb
def sum_all_water(b):
    ans = 0
    for l in b:
        for n in l:
            ans+=n
    return ans
def move_clouds(d,s):
    global clouds,n,m
    for i,cloud in enumerate(clouds):
        r,c = cloud
        # pdb.set_trace()
        nr = (n+r+dr[d]*s)%n
        nc = (n+c+dc[d]*s)%n
        clouds[i] = [nr,nc]
def rain(clouds):
    global board
    for r,c in clouds:
        board[r][c] +=1

def water_copy_bug(clouds):
    global board,dr,dc,n
    dif_board = [[0 for _ in range(n)] for _ in range(n)]
    for r,c in clouds:
        cnt =0
        for d in [1,3,5,7]:
            nr = r+dr[d]
            nc = c+dc[d]
            if 0<=nr<n and 0<=nc<n and board[nr][nc]>0:
                cnt+=1
        dif_board[r][c] += cnt
    for r in range(n):
        for c in range(n):
            board[r][c] += dif_board[r][c]
def get_new_clouds(b):
    global clouds,n
    new_clouds = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    for r,c in clouds:
        visited[r][c]=True
    for r in range(n):
        for c in range(n):
            if board[r][c]>=2 and visited[r][c]==False:
                new_clouds.append([r,c])
                board[r][c]-=2
    return new_clouds
def print_board(b):
    for l in b:
        print(l)
    print("="*10)
dr = [0,-1,-1,-1,0,1,1,1]
dc = [-1,-1,0,1,1,1,0,-1]

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
for i in range(m):
    # print("start 비바라기")
    d,s = map(int,input().split())
    move_clouds(d-1,s)
    rain(clouds)
    # print_board(board)
    water_copy_bug(clouds)
    # print_board(board)
    clouds = get_new_clouds(board)
print(sum_all_water(board))