# 累積和
MOD = 10 ** 9 + 7

def main():
    n = int(input())
    ans = 0

    a = list(map(int, input().split()))
    s = []
    s.append(a[0])

    for i in range(1, n):
        s.append((s[i - 1] + a[i]) % MOD)
        ans += (s[i - 1] * a[i])
        ans %= MOD

    print(ans)
main()
