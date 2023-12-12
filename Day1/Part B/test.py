def algo(i):
    s = str(i)
    first = ""
    first_index = -1
    last = ""
    last_index = -1
    num_names = ["1", "one", "2", "two", "3", "three", "4", "four", "5", "five", "6", "six", "7", "seven", "8", "eight",
                 "9", "nine"]
    for j in range(len(num_names)):
        if first_index == -1 or (first_index > s.find(num_names[j]) >= 0):
            first_index = s.find(num_names[j])
            if (num_names[j] == "one" or num_names[j] == "two" or num_names[j] == "three" or num_names[j] == "four" or
                    num_names[j] == "five" or num_names[j] == "six" or num_names[j] == "seven" or
                    num_names[j] == "eight" or num_names[j] == "nine"):
                first = num_names[j - 1]
            else:
                first = num_names[j]
        if last_index == -1 or (last_index < s.rfind(num_names[j]) >= 0):
            last_index = s.rfind(num_names[j])
            if (num_names[j] == "one" or num_names[j] == "two" or num_names[j] == "three" or num_names[j] == "four" or
                    num_names[j] == "five" or num_names[j] == "six" or num_names[j] == "seven" or
                    num_names[j] == "eight" or num_names[j] == "nine"):
                last = num_names[j - 1]
            else:
                last = num_names[j]

    result = int(first + last)
    return result


def main():
    f = open("input.txt", "r")
    result = 0
    for i in f:
        result = result + algo(i)
    print(result)


main()
