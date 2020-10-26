# 自力でできんかった

def main():
    n = int(input())

    w, z = [], []

    for _ in range(n):
        x, y = list(map(int, input().split()))
        z.append(x + y)
        w.append(x - y)

    ans = max(max(z) - min(z), max(w) - min(w))
    print(ans)

main()
