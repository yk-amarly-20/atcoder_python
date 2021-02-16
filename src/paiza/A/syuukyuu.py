def main():
    n = int(input())
    days = list(map(int, input().split()))

    first = days[:7]
    res = first.count(0)
    pointer = 7
