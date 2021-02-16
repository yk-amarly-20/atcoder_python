def main():
    n, x = list(map(int, input().split()))

    a = list(map(int, input().split()))
    for i in range(n):
        b = a[i]
        if b != x:
            print(b, end=" ")
    print("")

if __name__ == "__main__":
    main()
