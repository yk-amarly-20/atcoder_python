import math
def main():
    n, x, t = list(map(int, input().split()))

    print(math.ceil(n / x) * t)

main()
