filename = "Day5Input.txt"
textfile = open(filename, "r")
currentInput = textfile.read().strip()
unicodeCapital = ord('A')  # Gets the unicode value of uppercase 'A' - starting point for uppercase
unicodeLower = ord('a')  # Gets the unicode value of lowercase 'a' - starting point for lowercase


def opposite(a, b):
    if (a.lower() == b.lower()) and ((a.isupper() == b.islower()) or (a.islower() == b.isupper())):
        return True
    else:
        return False


def react(line):
    buffer = []
    for char in line:
        if buffer and opposite(char, buffer[-1]):
            buffer.pop()
        else:
            buffer.append(char)
    return len(buffer)


minimumLength = react(currentInput)  # Gets the length of polymer reacted normally

for letter in range(0, 26):
    tempInput = currentInput
    tempInput = tempInput.replace(chr(unicodeCapital + letter), "")
    tempInput = tempInput.replace(chr(unicodeLower + letter), "")
    tempLength = react(tempInput)
    if tempLength < minimumLength:
        minimumLength = tempLength

print(minimumLength)