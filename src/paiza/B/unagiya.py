# https: // paiza.jp/works/mondai/skillcheck_sample/long-table?language_uid = python3
import numpy as np

def main(seat):
    for i in range(m):
        a, b = list(map(int, input().split()))
        check_seat_or_not(a, b, seat)

    ans = count_free_seat(seat)
    print(ans)

def check_seat_or_not(a: int, b: int, seat) -> None:
    edokko = np.zeros(n, dtype=np.int)
    # b = 1, a = 3, n = 4はギリok
    if b + a <= n:
        edokko[b:a + b] = 1
    else:
        edokko[b:] = 1
        edokko[:a - n + b] = 1

    seat_nand = np.logical_not(seat & edokko)
    if seat_nand.all():
        seat += edokko

    return

def count_free_seat(seat) -> int:
    return len(np.where(seat == 1)[0])

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    seat = np.zeros(n, dtype=np.int)
    main(seat)
