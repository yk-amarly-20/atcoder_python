def main():
    n, k = list(map(int, input().split()))
    new_length = n // k
    small_image = []
    image = []

    for _ in range(n):
        x = list(map(int, input().split()))
        image.append(x)

    for i in range(new_length):
        small_list = []
        for j in range(new_length):
            res = 0
            for l in range(i * k, (i + 1) * k):
                res += sum(image[l][j * k: (j + 1) * k])
            small_list.append(res // (k ** 2))

        small_image.append(small_list)

    if new_length == 1:
        print(small_image[0][0])
    else:
        for i in range(new_length):
            for j in range(new_length - 1):
                print(small_image[i][j], end=" ")
            print(small_image[i][new_length - 1])

if __name__ == "__main__":
    main()
