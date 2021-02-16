def main():
    cards = list(input())
    card_counter = {}
    ans = 0
    for card in cards:
        if card not in card_counter.keys():
            card_counter[card] = 1
        else:
            card_counter[card] += 1

    key = card_counter.keys()
    if "*" not in key:
        if len(key) == 4:
            ans = 0
        elif len(key) == 3:
            ans = 1
        elif len(key) == 2:

            if card_counter[cards[0]] == 2:
                ans = 2
            else:
                ans = 3
        else:
            ans = 4
    else:
        if len(key) == 4:
            ans = 1
        elif len(key) == 3:
            ans = 3
        else:
            ans = 4

    judge_dict = {0: "NoPair", 1: "OnePair", 2: "TwoPair", 3: "ThreeCard", 4: "FourCard"}
    print(judge_dict[ans])

if __name__ == "__main__":
    main()
