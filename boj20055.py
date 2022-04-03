# boj 20055 컨베이어 벨트 위의 로봇
# 1번 위치에 올린다. N번 위치에 내린다.
# 1) 벨트가 로봇과 함께 1칸 회전한다.
# 2) 가장 먼저 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 한칸 이동할 수 있음 이동한다.
# 2-1) 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없고, 그 칸에 내구도가 1 이상 남아있어야한다.
# 3) 올리는 위치에 있는 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 4) 내구도가 0인 칸의 개수가 k개 이상이라면 종료한다.
# 5) 로봇을 올리는 위치에 올리거나 로봇이 어떤 칸으로 이동하면 그 칸의 내구도는 즉시 1만큼 감소한다.
import pdb
def rotate():
    global robots, belt, count,n
    belt.rotate(1)
    d_l = []
    for i,robot in enumerate(robots):
        robots[i] = (robot+1)%(2*n)
        if robots[i] == n-1:
            d_l.append(i)
    for i in d_l:
        del robots[i]
def no_robot_in(loc):
    global robots
    for robot in robots:
        if robot == loc:
            return False
    return True
def move_robot(idx, robot_loc):
    global robots, belt, count, n, del_list
    n_loc = (robot_loc+1)%(2*n)
    if belt[n_loc]>0 and no_robot_in(n_loc):
        robots[idx] = n_loc
        belt[n_loc]-=1
        if belt[n_loc]==0:
            count+=1
        if robots[idx]== n-1:
            del_list.append(idx)


def load_robot():
    global robots, belt, count
    robots.append(0)
    belt[0]-=1
    if belt[0]==0:
        count+=1
from collections import deque
robots = deque()
belt = deque()
n, k = map(int,input().split())
a = list(map(int,input().split()))
for i,aa in enumerate(a):
    belt.append(aa)
level = 0
count = 0
while count<k:
    level +=1
    rotate()
    del_list = []
    for idx, robot_loc in enumerate(robots):
        move_robot(idx, robot_loc)
    for i in del_list:
        del robots[i]
    if belt[0]>0:
        load_robot()
print(level)