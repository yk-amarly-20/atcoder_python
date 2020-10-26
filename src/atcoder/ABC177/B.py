def main():

    s = input()
    t = input()

    ans = len(t)

    for i in range(len(s) - len(t)):
        dif = 0
        for j in range(len(t)):
            if (s[i + j] != t[j]):
                dif += 1
        ans = min(ans, dif)

    print(ans)
main()
