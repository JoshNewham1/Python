filename = "Day5Input.txt"
textfile = open(filename, "r")
currentInput = textfile.read().strip()
oldInput = None
unicodeCapital = ord('A')  # Gets the unicode value of uppercase 'A' - starting point for uppercase
unicodeLower = ord('a')  # Gets the unicode value of lowercase 'a' - starting point for lowercase

while oldInput != currentInput:
    oldInput = currentInput
    for i in range(0, 26):
        # Removes combinations of capital and lowercase e.g 'Aa'
        currentInput = currentInput.replace(chr(unicodeCapital + i) + chr(unicodeLower + i), "")
        # Removes combinations of lowercase and capital e.g 'aA'
        currentInput = currentInput.replace(chr(unicodeLower + i) + chr(unicodeCapital + i), "")

print(len(currentInput))
