def algo(i):
    result = 0
    game_number = ""
    red = 12
    green = 13
    blue = 14
    game = i.split(": ")
    round = []
    color = []
    valid_game = True

    # Extract the game number from the first part of the split
    for j in game[0]:
        if j.isdigit():
            game_number = game_number + j

    # Get list of rounds
    round = game[1].split("; ")

    # Split out rounds
    for k in range(len(round)):
        round[k] = round[k].strip()
        color = round[k].split(", ")
        for m in range(len(color)):
            color_number = ""
            for l in color[m]:
                if l.isdigit():
                    color_number = color_number + l
            if color[m].find("red") != -1:
                if int(color_number) > red:
                    valid_game = False
                    break
            elif color[m].find("green") != -1:
                if int(color_number) > green:
                    valid_game = False
                    break
            elif color[m].find("blue") != -1:
                if int(color_number) > blue:
                    valid_game = False
                    break

    if valid_game:
        result = int(game_number)
    return result


def main():
    f = open("input.txt", "r")
    result = 0
    for i in f:
        result = result + algo(i)
    print(result)


main()
