from collections import deque
n=int(input())
a=[list(map(int,input().split())) for i in range(n)]

ans=1e9

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def get_ans(one,two,three,four,five):
    max_val=max(one,two,three,four,five)
    min_val=min(one,two,three,four,five)
    return max_val-min_val

def bfs(x,y,g):
    global n,b
    q=deque()
    q.append((x,y))
    b[x][y]=g
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<n and b[nx][ny]==0:
                q.append((nx,ny))
                b[nx][ny]=g

for x in range(n):
    for y in range(n):
        for d1 in range(1,n):
            for d2 in range(1, n):
                if 0<=y-d1 and y+d2<n:
                    if x+d1+d2<n:
                        b = [[0] * (n) for _ in range(n)]
                        one,two,three,four,five=0,0,0,0,0
                        #2.  경계선
                        #2.1. (x, y), (x+1, y-1), ..., (x+d1, y-d1)
                        for i in range(d1+1):
                            b[x+i][y-i]=5
                        #2.2. (x, y), (x+1, y+1), ..., (x+d2, y+d2)
                        for i in range(d2+1):
                            b[x+i][y+i]=5
                        #2.3. (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
                        for i in range(d2+1):
                            b[x+d1+i][y-d1+i]=5
                        #2.4. (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
                        for i in range(d1+1):
                            b[x+d2+i][y+d2-i]=5
                        #4. 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호
                        #4.3. 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
                        for j in range(y-d1-1,-1,-1):
                            b[x+d1][j]=3
                        #4.1.  1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
                        for i in range(x-1,-1,-1):
                            b[i][y]=1
                        #4.2. 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
                        for j in range(y+d2+1,n):
                            b[x+d2][j]=2
                        #4.4. 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
                        for i in range(x+d1+d2+1,n):
                            b[i][y-d1+d2]=4
                        bfs(0,0,1)
                        bfs(0,n-1,2)
                        bfs(n-1,0,3)
                        bfs(n-1,n-1,4)
                        #3. 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구
                        for i in range(n):
                            for j in range(n):
                                if b[i][j]==0:
                                    b[i][j]=5
                        for i in range(n):
                            for j in range(n):
                                if b[i][j]==1: one+=a[i][j]
                                elif b[i][j]==2: two+=a[i][j]
                                elif b[i][j]==3: three+=a[i][j]
                                elif b[i][j]==4: four+=a[i][j]
                                else: five+=a[i][j]
                        ans=min(ans,get_ans(one,two,three,four,five))
print(ans) 