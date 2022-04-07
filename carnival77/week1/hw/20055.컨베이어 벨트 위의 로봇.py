from collections import deque

n,k=map(int,input().split())

a=deque(list(map(int,input().split())))
r=deque([False]*2*n)
zeros=0
stage=0
up=0
down=n-1

def out():
    global r

    if r[down]:
        r[down]=False

while True:
    stage+=1

    #1
    a.rotate(1)
    r.rotate(1)
    out()

    #2
    for i in range(n-2,-1,-1):
        if r[i]:
            #2.1
            if r[i+1]==False and a[i+1]>=1:
                r[i+1],r[i] = r[i],r[i+1]
                a[i+1]-=1
                if a[i+1]==0:
                    zeros+=1
    out()
    #3
    if a[0]>0:
        r[0]=True
        a[0]-=1
        if a[0]==0:
            zeros+=1

    #4
    if zeros>=k:
        break
print(stage)