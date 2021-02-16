from collections import deque

def main():
    n, m = list(map(int, input().split()))
    maze = []
    sx, sy, gx, gy = -1, -1, -1, -1

    for i in range(m):
        # まず入力を処理しながらsを探す
        x = input().split()
        if "s" in x:
            sx, sy = x.index("s"), i
        elif "g" in x:
            gx, gy = x.index("g"), i
        maze.append(x)

    dp = [["Fail"] * n for _ in range(m)]
    que = deque([])

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    que.append([sx, sy])
    dp[sy][sx] = 0

    while que:
        p = que.popleft()

        if (p[0] == gx) and (p[1] == gy):
            break

        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) and (maze[ny][nx] != "1") and (dp[ny][nx] == "Fail"):
                dp[ny][nx] = dp[p[1]][p[0]] + 1
                que.append([nx, ny])

    print(dp[gy][gx])

if __name__ == "__main__":
    main()
