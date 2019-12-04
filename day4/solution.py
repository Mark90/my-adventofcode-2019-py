def part1_check(string):
    repetition = False
    for i in range(5):
        if string[i] > string[i + 1]:
            return False
        if string[i] == string[i + 1]:
            repetition = True
    return repetition


def part1(lines):
    number, stop = map(int, lines[0].split("-"))
    count = 0
    while number < stop:
        if part1_check(str(number)):
            count += 1
        number += 1
    print("[part1] Count is", count)


def part2_check(string):
    repetition = exactly_two = False
    prev = ""
    for i in range(5):
        cur, nex = string[i : i + 2]
        if cur > nex:
            return False

        if exactly_two:
            continue  # only need to check no cur > nex

        try:
            if repetition:
                if prev != nex:
                    exactly_two = True
                    continue
                repetition = False
            elif cur == nex and nex != prev:
                if i == 4:
                    return True
                repetition = True
        finally:
            prev = cur

    if repetition and exactly_two:
        return True


def part2(lines):
    number, stop = map(int, lines[0].split("-"))
    count = 0
    while number < stop:
        if part2_check(str(number)):
            count += 1
        number += 1
    print("[part2] Count is", count)
