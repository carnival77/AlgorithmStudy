n,m = map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]

moves=[]

for i in range(m):
    d,s = map(int,input().split())
    moves.append([d-1,s])

dir = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]

diagonals = [[-1,-1],[-1,1],[1,-1],[1,1]]

c1 = [[False] * (n) for _ in range(n)]
c2 = [[False] * (n) for _ in range(n)]
c1[n-1][0] = c1[n-1][1] = c1[n-2][0] = c1[n-2][1] = True

for d,s in moves:
    pw = [[False] * (n) for _ in range(n)]  # 2에서 물이 증가한 칸
    c2 = [[False] * (n) for _ in range(n)] # 2에서 구름이 있었던 칸
    # 1. 모든 구름이 di 방향으로 si칸 이동한다.
    for x in range(n):
        for y in range(n):
            if c1[x][y]:
                dx,dy=dir[d]
                nx,ny = (x+dx*s+n)%n,(y+dy*s+n)%n

                c2[nx][ny]=True

                # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
                a[nx][ny]+=1
                pw[nx][ny]=True
    c1=c2

    # 3. 구름이 모두 사라진다.
    c1 = [[False] * (n) for _ in range(n)]

    # 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다.
    # 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    for x in range(n):
        for y in range(n):
            if pw[x][y]:
                for dx,dy in diagonals:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<n and 0<=ny<n:
                        if a[nx][ny]>0:
                            a[x][y]+=1


    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for x in range(n):
        for y in range(n):

            if a[x][y]>=2 and c2[x][y]==False:
                c1[x][y]=True
                a[x][y]-=2
ans=0
for x in range(n):
    for y in range(n):
        ans+=a[x][y]
print(ans)