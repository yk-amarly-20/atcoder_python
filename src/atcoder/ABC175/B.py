# 全探索
import sys

def main():
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0

    if n <= 2:
        print(0)
        sys.exit()

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if len(set([l[i], l[j], l[k]])) < 3:
                    continue

                if abs(l[i] - l[j]) < l[k] < (l[i] + l[j]):
                    ans += 1
    print(ans)
main()
