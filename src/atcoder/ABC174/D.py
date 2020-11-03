def main():

    _ = int(input())
    colors = list(input())

    ans = 0
    red_count = colors.count("R")
    for i in range(red_count):
        if colors[i] == "W":
            ans += 1

    print(ans)
main()
