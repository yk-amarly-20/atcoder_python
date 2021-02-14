def main():
    h, w = list(map(int, input().split()))
    garden = []
    garden.append(['.'] * (w + 1))
    for _ in range(h):
        x = list(input())
        x.insert(0, ".")
        x.append('.')
        garden.append(x)
    garden.append(['.'] * (w + 1))

    ans = 0

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if garden[i][j] == "#":
                surrounded = [garden[i + 1][j], garden[i - 1][j], garden[i][j + 1], garden[i][j - 1]]
                ans += (4 - surrounded.count("#"))

    print(ans)

if __name__ == "__main__":
    main()
