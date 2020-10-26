MOD = 10**9 + 7

def main():
    # 答えは10**n - 2 * 9 ** n + 8 ** n

    n = int(input())

    ans = 1

    for _ in range(n):
        ans = (ans * 10) % MOD

    res = 1
    for _ in range(n):
        res = (res * 9) % MOD
    res = (res * 2) % MOD

    ans = (ans - res) % MOD

    res = 1
    for _ in range(n):
        res = (res * 8) % MOD
    ans = (ans + res) % MOD

    print(ans)

main()
