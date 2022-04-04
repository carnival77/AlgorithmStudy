# 피드백
# 1. 내구도가 마이너스 될 때마다 stop할 지 여부를 체크하면 된다.

import sys

input=sys.stdin.readline

n,k = map(int,input().split())

TN=2*n

a=list(map(int,input().split()))

c = [False] * (TN)
stage=0
zeros = 0  #내구도가 0인 칸의 개수

def out():
    if c[n - 1] == True:
        c[n - 1] = False

while True:
    stage += 1
    #1

    # a=a[-1:] + a[:-1]
    # c=c[-1:]+c[:-1]

    temp1 = a[TN-1]
    temp2 = c[TN-1]
    for i in range(TN-1,0,-1):
        a[i]=a[i-1]
        c[i]=c[i-1]
    a[0]=temp1
    c[0]=temp2
    # print
    out()
    # if c[n - 1] == True:
    #     c[n - 1] = False
    #2
    for i in range(n-2,-1,-1):
        if c[i]==True:
            #2.1
            if c[i+1]==False and a[i+1]>0:
                c[i+1]=c[i]
                c[i]=False
                a[i+1]-=1
                # 내구도 체크
                if a[i+1] == 0:
                    zeros+=1

    out()
    # if c[n - 1] == True:
    #     c[n - 1] = False
    #3
    if a[0]>0:
        c[0]=True
        a[0]-=1
        if a[0] == 0:
            zeros+=1
    #4
    if zeros >= k:
        print(stage)
        break