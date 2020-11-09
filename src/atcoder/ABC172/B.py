def main():
    s = list(input())
    t = list(input())
    length = len(s)
    ans = 0

    for i in range(length):
        if s[i] != t[i]:
            ans += 1

    print(ans)
main()
