import math
def main():
    n, m = list(map(int, input().split()))
    tree = list(map(int, input().split()))
    q = int(input())

    for i in range(q):
        s, e = list(map(int, input().split()))
        length = e - s + 1
        num_elec = 0
        for j in range(s - 1, e):
            num_elec += tree[j]
        res = math.ceil((m * length - num_elec) / length)
        if res <= 0:
            continue
        else:
            for j in range(s - 1, e):
                tree[j] += res

    for i in range(n):
        print(tree[i], end=" ")

    print("")

if __name__ == "__main__":
    main()
