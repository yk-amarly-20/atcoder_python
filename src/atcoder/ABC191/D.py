from typing import Tuple
import math

def main():
    # 普通にやると浮動少数点誤差で死ぬ
    # 10^4倍すれば解決
    x, y, r = list(map(float, input().split()))
    ratio = 10 ** 4
    x = int(x *  ratio)
    y = int(y * ratio)
    r = int(r * ratio)

    def count_lattice_point(centerX: int, centerY: int, r: int):

        lattie = 0
        for i in range(centerX + 1, centerX + r):
            top = math.floor(math.sqrt(r ** 2 - (i - centerX) ** 2) + centerY)
            lattie = 4 * (top - centerY + 1)

        lattie += 4 * r + 1

        return lattie

    lattie = count_lattice_point(x, y, r)

    print(lattie)

if __name__ == "__main__":
    main()
