import math
def main():

    n, d = list(map(int, input().split()))
    ans = 0

    for _ in range(n):
        x, y = list(map(int, input().split()))
        distance = math.sqrt(x ** 2 + y ** 2)
        if distance <= d:
            ans += 1

    print(ans)
main()
