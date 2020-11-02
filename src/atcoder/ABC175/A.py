def main():

    s = input()

    if (s == "RRR"):
        print(3)
    elif (s == "RSS") or (s == "SRS") or (s == "SSR") or (s == "RSR"):
        print(1)
    elif (s == "RRS") or (s == "SRR"):
        print(2)
    else:
        print(0)

main()
