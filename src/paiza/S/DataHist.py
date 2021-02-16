def main():

    counter = {}
    s = input()
    length = len(s)
    index = 0
    suuji = False  # 今のindexが数字かどうか
    moji = False  # 今のindexが文字かどうか
    kakko = False  # 今のindexはかっこ内かどうか
    while index < length:
        pass



    def update(c: str, num: int):
        if c in counter.keys():
            counter[c] += num
        else:
            counter[c] = num
