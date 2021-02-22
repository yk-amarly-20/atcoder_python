import math

def main():
    k = int(input())
    # 全部同じパターン
    same_all = math.floor(k ** (1 / 3))
    # 二つ同じパターン
    same_two = 0
    for i in range(1, int(math.sqrt(k)) + 1):
        same_two += int(k / (i ** 2))
    same_two *= 3
    same_two -= (3 * same_all)

    # 全部違うパターン
    res = 0
    df = 0
    for a in range(1, math.floor(k ** (1 / 3)) + 1):    #aの値
        res = int(k / a)
        if (a + 1 > int(res / a)):
            continue
        for b in range(a + 1, int(res / a)):    # bの値
            if (int(res / b) <= b):
                continue
            df += (int(res / b) - b)

    ans = same_all + (df * 6) + same_two

    print(ans)


if __name__ == "__main__":
    main()
