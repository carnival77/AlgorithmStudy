n,m,t = map(int,input().split())

#우,하,좌,상 - 시계 방향
dx=[0,-1,0,1]
dy=[1,0,-1,0]

a=[list(map(int,input().split())) for i in range(n)] # 원본 보드
b=[[0] * m for _ in range(n)] # 확산될 미세먼지들의 합을 저장해놓는 보드

ax,ay=0,0 # 공기청정기 2칸 중 위쪽 칸 위치
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
             ax=i
             ay=j

ax-=1

# 시작점(공기청정기 위치)과 시계/반시계 방향을 매개변수로 받는다.
def air_clean(sx,sy,z):
    prev=0
    x=sx
    y=sy+1 # 공기청정기 오른쪽 칸부터 탐색
    k=0 # 방향 인덱스

    while True:
        # 탐색 인덱스가 시작점(공기청정기 위치)에 다다르면 break
        if sx==x and sy==y:
            break
        temp=prev
        prev=a[x][y]
        a[x][y]=temp
        x+=dx[k]
        y+=dy[k]
        # if x < 0 or y < 0 or x >= n or y >= m:
        if not 0<=x<n or not 0<=y<m:
            x-=dx[k]
            y-=dy[k]
            k=(k+z)%4
            x+=dx[k]
            y+=dy[k]

for _ in range(t):
    for x in range(n):
        for y in range(m):
            if a[x][y]<=0:
                continue
            diffuse_target=[] # 미세먼지가 확산될 칸 리스트
            for k in range(4):
                nx,ny = x+dx[k],y+dy[k]
                # 만약 범위 내이고 공기청정기가 아니라면
                if 0<=nx<n and 0<=ny<m and a[nx][ny]>=0:
                    diffuse_target.append([nx,ny])
            # 미세먼지가 확산되야 할 칸이 존재한다면
            if len(diffuse_target)>0:
                diffusion = a[x][y]//5
                # 저장 보드에 미세먼지 값을 더하고
                for tx,ty in diffuse_target:
                    b[tx][ty]+=diffusion
                # 원본 보드의 해당 칸에서는 미세먼지를 줄인다
                a[x][y]-=diffusion*len(diffuse_target)

    # 저장 보드의 미세먼지를 원본 보드에 합한다.
    for x in range(n):
        for y in range(m):
            if a[x][y]==-1:
                continue
            a[x][y] += b[x][y]
            b[x][y]=0

    # 공기청정기 윗칸. 반시계 방향
    air_clean(ax,ay,1)
    # 공기청정기 아래칸. 시계 방향
    air_clean(ax+1,ay,3)

ans=0
for i in range(n):
    for j in range(m):
        if a[i][j]>=0:
            ans+=a[i][j]

print(ans)