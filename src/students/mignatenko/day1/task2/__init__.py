def main():
    r = []
    a1 = ["strong", "arp", "live"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    #a1 = ["tarp", "mice", "bull"]
    #a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    for x in a1:
        for y in a2:
            if x in y:
                if x not in r: r.append(x)
    print(sorted(r))


if __name__ == "__main__":
    main()
