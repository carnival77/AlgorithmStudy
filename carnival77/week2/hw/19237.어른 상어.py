#1. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다
#2.  그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
#2.1. 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다
#2.2. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다
#3.  1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지

#상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,smell_time = map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
shark=[[0]*n for _ in range(n)] # 상어 번호별 위치
shark_next=[[0]*n for _ in range(n)] # 다음에 위치하게 될 상어의 위치
smell=[[0]*n for _ in range(n)] # 냄새
smell_who=[[0]*n for _ in range(n)] # 누구의 냄새?
priority = [[[0]*4 for _ in range(4)] for __ in range(m+1)] # priority[i][j][k] : i번 상어의 방향이 j일 때 4개의 우선 순위 중 k번째 방향
#  우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.

for x in range(n):
    for y in range(n):
        if a[x][y]>0:
            shark[x][y]=a[x][y]
            smell[x][y]=smell_time
            smell_who[x][y]=a[x][y]

dirs=[0]+[d-1 for d in map(int,input().split())] # 상어의 번호별 현재 방향

for i in range(1,m+1):
    for j in range(4):
        priority[i][j]=[d-1 for d in map(int,input().split())]

#3. 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지
def check_1():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if shark[i][j] > 0:
                cnt += 1
    return cnt == 1

#2. 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다.
def move():
    sharks=[]
    for x in range(n):
        for y in range(n):
            shark_next[x][y]=0 # 다음에 위치하게 될 상어의 위치를 0으로 초기화한다.
            if shark[x][y]>0:
                sharks.append((shark[x][y],x,y))

    sharks.sort() # 번호가 작은 상어부터 움직인다.

    for s in sharks:
        num,sx,sy = s # 상어의 번호와 위치
        shark_d = dirs[num] # 상어의 현재 방향
        ok=False # 이동해야 할 칸 찾았으면 True

        for k in range(4): # 4가지 방향 중에서, 해당 상어의 번호에 부여된 우선 순위에서 현재 방향에 맞는 순위를 순차적으로 탐색한다.
            pd=priority[num][shark_d][k] #  우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
            nx=sx+dx[pd]
            ny=sy+dy[pd]
            #2.1. 인접한 칸 중 아무 냄새가 없는 칸 찾기
            if 0<=nx<n and 0<=ny<n and smell[nx][ny]==0:
                # 만약 이동할 칸에
                # 상어가 없다면
                if shark_next[nx][ny]==0:
                    shark_next[nx][ny]=num
                    dirs[num]=pd
                # 상어가 있는데, 현재 상어보다 번호가 크면 쫓겨난다
                else:
                    if shark_next[nx][ny]>num:
                        shark_next[nx][ny]=num
                        dirs[num]=pd
                # 이동했으면 종료
                ok=True
                break
            # 이동했으면 종료
            if ok:
                break

        # 2.1. 에서 이동 안 했으면,
        # 2.2. 자신의 냄새가 있는 칸의 방향으로 잡는다.
        if not ok:
            for k in range(4):
                pd = priority[num][shark_d][k]
                nx = sx + dx[pd]
                ny = sy + dy[pd]
                # 2.2. 인접한 칸 중 자신의 냄새가 있는 칸 찾기
                if 0 <= nx < n and 0 <= ny < n and smell[nx][ny] > 0 and smell_who[nx][ny]==num:
                    shark_next[nx][ny] = num
                    dirs[num] = pd
                    # 이동했으면 종료
                    ok = True
                    break
                # 이동했으면 종료
                if ok:
                    break

    for x in range(n):
        for y in range(n):
            # shark_next 에 저장되어 있는 예정된 칸으로 상어를 이동.
            shark[x][y]=shark_next[x][y]
            # smell 1씩 빼기
            if smell[x][y]>0:
                smell[x][y]-=1
            # smell 0 이면 smell_who 도 0으로
            if smell[x][y]==0:
                smell_who[x][y]=0
            # 상어 있는 칸에 smell, smell_who 상어 정보 및 smell_time으로 초기화
            if shark[x][y]>0:
                smell_who[x][y]=shark[x][y]
                smell[x][y]=smell_time
ans = -1
for t in range(1,1001):
    move()
    if check_1():
        ans = t
        break
print(ans)