# S = nのときの答えをA[n]

import sys

MOD = 10 ** 9 + 7

def main():
    s =int(input())

    ans = 0
    a = []
    a += [0, 0, 0, 1, 1, 1]

    if s <= 2:
        ans = a[s]

    else:
        for i in range(6, s + 1):
            a.append((a[i - 1] + a[i - 3]) % MOD)
        ans = a[s]

    print(ans)
main()
