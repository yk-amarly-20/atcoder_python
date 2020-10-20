# 繰り返し
# setの長さ使えば行けそうやなぁ

import sys

def main():
    n, x, m = list(map(int, input().split()))

    ans = 0
    ans += x
    a = list()
    b = set()
    a.append(x)
    b.add(x)
    j = 1

    while len(a) == len(b):  # 繰り返しが発生すると長さが変わる
        x = x * x % m
        ans += x
        a.append(x)
        b.add(x)
        j += 1
        if j == n:
            print(ans)
            sys.exit()

    repeat_index = a.index(x)
    repeat_length = len(a) - repeat_index - 1
    repeat_sum = sum(a[repeat_index:-1])
    repeat_times = (n - repeat_index) // repeat_length
    ans = ans - a[repeat_index] + repeat_sum * (repeat_times - 1)

    # ここまで繰り返し
    # ここから残りのとこを全部計算

    rest_num = n - repeat_index - repeat_times * repeat_length

    for i in a[repeat_index:repeat_index + rest_num]:
        ans += i

    print(ans)

main()
