def main():
    a, b, c = list(map(int, input().split()))
    b = b % 4
    c = c % 2
    a = a % 10

    b = (b ** c) % 4
    print((a ** b) % 10)



if __name__ == "__main__":
    main()
