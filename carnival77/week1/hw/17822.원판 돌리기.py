# 탐색 알고리즘 :
# 각 칸의 오른쪽과 아래쪽과 비교하여 같은 지 확인한다.
# check 배열로 같으면 True 로 하여, 탐색 중 원본 a를 안전하게 지킨다.
from collections import deque

n,m,t = map(int,input().split())

a=[None]

dx=[-1,0,1,0]
dy=[0,-1,0,1]

for i in range(n):
    d=deque(list(map(int,input().split())))
    a.append(d)

# 원판 회전
def rotation(x,d,k):
    global a

    # 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
    for i in range(1,n+1):
        if i%x==0:
            if d==0: # 시계 방향
                a[i].rotate(k)
            else: # 반시계방향
                a[i].rotate(-k)

# 인접한 수 중 같은 수 찾기
# 각 칸의 오른쪽과 아래쪽과 비교하여 같은 지 확인한다.
# check 배열로 같으면 True 로 하여, 탐색 중 원본 a를 안전하게 지킨다.
def find_adjacent_same():
    global a

    adjacent_same = False

    check=[[False]*m for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(m):
            if a[i][j]==0:
                continue
            if a[i][j]==a[i][(j+1)%m]:
                check[i][j] = check[i][(j+1)%m] = True
            if i+1<=n and a[i][j] == a[i+1][j]:
                check[i][j] = check[i+1][j] = True

    for i in range(1,n+1):
        for j in range(m):
            if check[i][j]:
                adjacent_same=True
                a[i][j]=0

    return adjacent_same

# 원판 위의 수의 평균 구하기
def get_avg():
    global a

    total_sum,cnt=0,0

    for i in range(1,n+1):
        for j in range(m):
            if a[i][j]!=0:
                total_sum+=a[i][j]
                cnt+=1

    if cnt == 0:
        return

    return total_sum/cnt

# 시뮬레이션
for _ in range(t):
    x,d,k = map(int,input().split())

    #1
    rotation(x, d, k)

    #2. 인접하면서 수가 같은 것을 모두 찾는다.
    # 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
    adjacent_same = find_adjacent_same()
    # 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
    if not adjacent_same:
         avg=get_avg()
         for i in range(1,n+1):
             for j in range(m):
                 if a[i][j]!=0:
                     if a[i][j]>avg:
                         a[i][j]-=1
                     elif a[i][j]<avg:
                         a[i][j]+=1

answer=sum(sum(row) for row in a[1:])

print(answer)