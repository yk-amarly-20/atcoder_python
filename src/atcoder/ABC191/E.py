import heapq

def main():
    INF = 1 << 60
    n, m = list(map(int, input().split()))
    abc = [tuple(map(int, input().split())) for _ in range(m)]
    road = [[] for _ in range(n)]
    for (a, b, c) in abc:
        road[a - 1].append((b - 1, c))

    def dijkstra(start: int, goal: int, edges):
        hq = [(0, start)]   # (まだ調査していない(コスト, 点))
        cost = [INF for _ in range(n)]
        cost[start] = 0
        res = INF

        while hq:
            c, x = heapq.heappop(hq)
            if c > cost[x]:
                continue
            for y, rc in edges[x]:
                y_cost = rc + cost[x]
                if y == goal:
                    res = min(res, y_cost)
                if y_cost < cost[y]:
                    cost[y] = y_cost
                    heapq.heappush(hq, (y_cost, y))

        return res

    for i in range(n):
        cost = dijkstra(i, i, road)
        if cost < INF:
            print(cost)
        else:
            print(-1)

if __name__ == "__main__":
    main()
