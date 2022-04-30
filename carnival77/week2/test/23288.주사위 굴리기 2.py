# 구현, DFS/BFS

from collections import deque

n,m,k = map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]

#  동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x,y = 0,0
d=0

dice = [1, 2, 3, 4, 5, 6]

ans=0

def bfs(x,y,b):
    c=[[False]*m for _ in range(n)]
    q=deque()
    q.append((x,y))
    c[x][y]=True
    cnt=0
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and a[nx][ny] == b and not c[nx][ny]:
                q.append((nx,ny))
                c[nx][ny]=True
                cnt+=1
    return cnt

for _ in range(k):
    #1
    if not 0<=x+dx[d]<n or not 0<=y+dy[d]<m:
        d=(d+2)%4
    x,y = x+dx[d],y+dy[d]

    #2
    ans+=(bfs(x,y,a[x][y])+1)*a[x][y]

    #3
    if d == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif d == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif d == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    if dice[5] > a[x][y]:
        d = (d + 1) % 4
    elif dice[5] < a[x][y]:
        d = (d + 3) % 4

print(ans)