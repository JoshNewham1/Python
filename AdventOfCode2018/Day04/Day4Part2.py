from collections import defaultdict

filename = "Day4Input.txt"
textfile = open(filename, "r")
puzzle_input = textfile.readlines()
puzzle_input.sort()  # Sort before beginning

minutesAsleep = defaultdict(int)


def parsetime(line):
    words = line.split()
    date = words[0][1:]
    time = words[1][:-1]
    return int(time.split(':')[1])  # Only return the minute (hour is irrelevant)


def maxvalue(dictionary):
    best = None
    for key, value in dictionary.items():
        if best is None or value > dictionary[best]:
            best = key
    return best


for line in puzzle_input:
    time = parsetime(line)
    if 'begins shift' in line:
        guardNumber = int(line.split()[3][1:])
        asleep = None
    elif 'falls asleep' in line:
        asleep = time
    elif 'wakes up' in line:
        for minute in range(asleep, time):
            minutesAsleep[(guardNumber, minute)] += 1


bestGuard, bestMinute = maxvalue(minutesAsleep)  # Gets the most frequent minute and finds the guard associated with it

print("Most frequent minute: " + str(bestMinute))
print("Guard associated with this minute: " + str(bestGuard))
print("Minute x Guard: " + str(bestMinute * bestGuard))