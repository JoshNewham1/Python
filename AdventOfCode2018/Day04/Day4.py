from collections import defaultdict

filename = "Day4Input.txt"
textfile = open(filename, "r")
puzzle_input = textfile.readlines()
puzzle_input.sort()  # Sort before beginning

minutesAsleep = defaultdict(lambda: defaultdict(int))
totalAsleep = defaultdict(int)


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
            minutesAsleep[guardNumber][minute] += 1
            totalAsleep[guardNumber] += 1


bestGuard = maxvalue(totalAsleep)
bestMinute = maxvalue(minutesAsleep[bestGuard])

print("Guard with most time slept: " + str(bestGuard))
print("Their most frequent minute to sleep was " + str(bestMinute))
print("Guard ID x Minute = " + str(bestGuard * bestMinute))