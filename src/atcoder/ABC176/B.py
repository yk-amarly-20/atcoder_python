MOD = 9
def main():
    n = list(input())
    ans = 0

    for i in n:
        ans = (ans + int(i)) % MOD

    print("Yes" if ans == 0 else "No")

main()
