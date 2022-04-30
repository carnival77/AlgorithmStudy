def move(a,col,type):
    ans=0
    max_row=-1
    n,m=len(a),len(a[0])
    # 블록을 놓을 위치를 빨간색 보드에서 선택하면, 그 위치부터 초록색 보드로 블록이 이동하고, 파란색 보드로 블록이 이동한다. 블록의 이동은 다른 블록을 만나거나 보드의 경계를 만나기 전까지 계속해서 이동
    for i in range(n):
        if a[i][col]==0:
            max_row=i
        else:
            break
    if type==2:
        max_row2=-1
        for i in range(n):
            if a[i][col+1]==0:
                max_row2=i
            else:
                break
        max_row=min(max_row,max_row2)
    a[max_row][col]=1
    if type==2:
        a[max_row][col+1]=1
    if type==3:
        a[max_row-1][col]=1
    # 행은 모든 칸이 타일로 가득 차있다. 이렇게 초록색 보드에서 어떤 행이 타일로 가득 차 있다면, 그 행의 타일은 모두 사라진다. 사라진 이후에는 초록색 보드에서 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동한다. 파란색의 경우는 열이 타일로 가득 차 있으면, 그 열의 타일이 모두 사라지며, 사라진 이후에는 파란색 보드에서 사라진 열의 왼쪽에 있는 블록이 사라진 열의 수만큼 오른쪽으로 이동한다. 이렇게 한 행이나 열이 타일로 가득 차서 사라지면 1점을 획득한다. 점수는 사라진 행 또는 열의 수와 같다
    deleted_row=-1
    for i in range(n):
        ok=True
        for j in range(m):
            if a[i][j]==0:
                ok=False
        if ok:
            if deleted_row<i:
                deleted_row=i
            ans+=1
            for j in range(m):
                a[i][j]=0
    if ans>0:
        for i in range(deleted_row,-1,-1):
            for j in range(m):
                a[i][j]=0
                if i-ans>=0:
                    a[i][j] = a[i - ans][j]
            # if i-ans>=0:
            #     a[i] = a[i - ans]
    # 초록색 보드의 0, 1번 행과 파란색 보드의 0, 1번 열은 그림에는 연한색으로 표현되어 있는 특별한 칸이다. 초록색 보드의 0, 1번 행에 블록이 있으면, 블록이 있는 행의 수만큼 아래 행에 있는 타일이 사라지고, 초록색 보드의 모든 블록이 사라진 행의 수만큼 아래로 이동하고, 파란색 보드의 0, 1번 열에 블록이 있으면, 블록이 있는 열의 수만큼 오른쪽 열에 있는 타일이 사라지고, 파란색 보드의 모든 블록이 사라진 열의 수만큼 이동하게 된다.
    cnt=0
    for i in range(2):
        exist=False
        for j in range(m):
            if a[i][j]==1:
                exist=True
        if exist:
            cnt+=1
    if cnt>0:
        for i in range(n-1,-1,-1):
            for j in range(m):
                a[i][j]=0
                if i-cnt>=0:
                    a[i][j]=a[i-cnt][j]
            # if i-cnt>=0:
            #     a[i]=a[i-cnt]
    return ans

ans=0
b=[[0]*4 for i in range(6)]
g=[[0]*4 for i in range(6)]
N=int(input())
n,m=len(b),len(b[0])
for i in range(N):
    t,x,y=map(int,input().split())
    if t==1:
        ans+=move(g,y,1)
        ans+=move(b,x,1)
    elif t==2:
        ans+=move(g,y,2)
        ans+=move(b,x,3)
    else:
        ans+=move(g,y,3)
        ans+=move(b,x,2)
cnt=0
for i in range(n):
    for j in range(m):
        if b[i][j]!=0:
            cnt+=1
        if g[i][j]!=0:
            cnt+=1
print(ans)
print(cnt)