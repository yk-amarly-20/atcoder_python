def main():

    h, w, k = list(map(int, input().split()))
    c = []
    ans = 0

    for i in range(h):
        c_tmp = list(input())
        c.append(c_tmp)

    H_range = range(0, (1 << h))
    W_range = range(0, (1 << w))

    for mask_H in H_range:
        for mask_W in W_range:
            blask_num = 0

            for i in range(h):
                for j in range(w):
                    if (((mask_H >> i) & 1) == 0) and (((mask_W >> j) & 1) == 0) and (c[i][j] == '#'):
                        blask_num += 1

            if blask_num == k:
                ans += 1
    print(ans)

main()
