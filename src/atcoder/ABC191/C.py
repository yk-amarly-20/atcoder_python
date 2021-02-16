def main():
    def count_sharp(y: int, x: int):
        a = 0
        if square[y][x] == "#":
            a += 1
        if square[y][x + 1] == "#":
            a += 1
        if square[y + 1][x] == "#":
            a += 1
        if square[y + 1][x + 1] == "#":
            a += 1

        return a

    height, weight = list(map(int, input().split()))
    square = []

    for i in range(height):
        x = list(input())
        square.append(x)

    ans = 0

    for i in range(height - 1):
        for j in range(weight - 1):

            num = count_sharp(i, j)
            if num % 2 == 1:
                ans += 1

    print(ans)

if __name__ == "__main__":
    main()
