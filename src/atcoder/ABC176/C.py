import sys
def main():

    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    if n == 1:
        print(0)
        sys.exit()

    max_len = a[0]

    for i in range(1, n):
        ans += max(max_len - a[i], 0)
        max_len = max(max_len, a[i])

    print(ans)

main()
