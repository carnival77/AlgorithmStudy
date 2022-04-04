import sys

# 우,하,좌,상
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
n, m, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [[0] * m for _ in range(n)]

x = 0
y = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            x = i
            y = j
x -= 1


def go(sx, sy, z):
    prev = 0
    x = sx
    y = sy + 1
    k = 0
    while True:
        if x == sx and y == sy:
            break
        temp = prev
        prev = a[x][y]
        a[x][y] = temp
        x += dx[k]
        y += dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            x -= dx[k]
            y -= dy[k]
            k += z
            k %= 4
            x += dx[k]
            y += dy[k]


for _ in range(t):
    for i in range(n):
        for j in range(m):
            if a[i][j] <= 0:
                continue
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and a[nx][ny] >= 0:
                    cnt += 1
            if cnt > 0:
                val = a[i][j] // 5
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and a[nx][ny] >= 0:
                        b[nx][ny] += val
                a[i][j] = a[i][j] - cnt * val

    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                continue
            a[i][j] += b[i][j]
            b[i][j] = 0
    go(x, y, 1)
    go(x + 1, y, 3)

ans = 0

for i in range(n):
    for j in range(m):
        if a[i][j] >= 0:
            ans += a[i][j]
print(ans)