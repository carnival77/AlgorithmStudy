"""
원판 돌리기

1. 원판 돌리기
2. 숫자 지우기
2-1. 인접하고 같은 숫자 찾기
2-2. 인접하고 같은 숫자 있으면, 지우기
2-3. 하나도 없으면, 평균 구하고, 평균보다 크면 -1, 작으면 +1
"""
import pdb
from collections import deque
def add_numbers(l):
    ans = 0
    for q in l:
        for i in range(len(q)):
            ans += q[i]
    return ans
def print_plates():
    global plates
    for plate in plates:
        print(plate)
    print("="*10)
def rotate_plates(x,d,k):
    global plates,N,M
    if d == 1: # counter clockwise
        k *= -1
    for n in range(N):
        if (n+1)%x == 0:
            plates[n].rotate(k)
def delete_numbers(l):
    global plates
    for r, c in l:
        plates[r][c] =0
def change_numbers():
    global plates, N,M
    flag = False
    visited = [[False for _ in range(M)] for _ in range(N)]
    for n, plate in enumerate(plates):
        for m in range(M):
            # pdb.set_trace()
            if visited[n][m]==False and plate[m]>0:
                q = deque()
                number = plate[m]
                l = [[n,m]]
                q.append([n,m])
                visited[n][m]=True
                while q:
                    cr, cc = q.popleft()
                    dr = [0,0,1,-1]
                    dc = [1,-1,0,0]
                    for d in range(4):
                        nr = cr+dr[d]
                        nc = cc+dc[d]
                        if 0<=nr<N:
                            if nc<0:
                                nc = M-1
                            if nc >M-1:
                                nc = 0
                            if plates[nr][nc]==number and visited[nr][nc]==False:
                                q.append([nr,nc])
                                l.append([nr,nc])
                                visited[nr][nc]=True
                if len(l)>1:
                    delete_numbers(l)
                    flag =True
    if flag==False:
        s = 0
        cnt=0
        for plate in plates:
            for num in plate:
                if num>0:
                    cnt+=1
                s+=num
        if cnt>1:
            avg = s/cnt
            for n, plate in enumerate(plates):
                for m, num in enumerate(plate):
                    if num>0:
                        if num>avg:
                            plates[n][m] = plates[n][m]-1
                        elif num<avg:
                            plates[n][m]= plates[n][m]+1

N,M,T = map(int,input().split())
plates = [deque() for _ in range(N)]
for i in range(N):
    l = list(map(int,input().split()))
    for num in l:
        plates[i].append(num)
for t in range(T):
    x, d, k = map(int,input().split())
    rotate_plates(x,d,k)
    # print_plates()
    change_numbers()
    # print_plates()
# print_plates()
print(add_numbers(plates))
