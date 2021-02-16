def main():
    v, t, s, d = list(map(int, input().split()))
    if (v * t <= d <= v * s):
        print("No")
    else:
        print("Yes")

if __name__ == "__main__":
    main()
