def algo(i):
    s = str(i)
    j = ""
    result = ""
    for k in s:
        if k.isdigit():
            j = j + k
    result = result + j[0] + j[len(j) - 1]
    return int(result)


def main():
    f = open("input.txt", "r")
    result = 0
    for i in f:
        result = result + algo(i)
    print(result)


main()
