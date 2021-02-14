def main():
    n, s = input().split()
    n = int(n)
    key = list(s)
    key_list = {}
    for i in range(26):
        alpha = chr(ord('a') + i)
        key_list[key[i]] = alpha

    code = input().split()
    for _ in range(n):
        ans = []
        for s in code:
            s_list = list(s)
            s_comp = ''
            for c in s_list:
                c = key_list[c]
                s_comp += c
            ans.append(s_comp)
            code = ans

    for s in ans[:-1]:
        print(s, end=" ")
    print(ans[-1])

if __name__ == "__main__":
    main()
