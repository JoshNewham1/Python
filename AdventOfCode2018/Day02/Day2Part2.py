from difflib import SequenceMatcher

filename = "Day2Input.txt"
textfile = open(filename, "r")
puzzle_input = textfile.readlines()
foundResult = False

for firstItem in puzzle_input:
    for secondItem in puzzle_input:
        probOfOneLetterDifferent = (len(firstItem)-1) / len(secondItem)

        likeness = SequenceMatcher(None, firstItem, secondItem)

        if likeness.ratio() == probOfOneLetterDifferent:
            print(firstItem)
            print(secondItem)
            foundResult = True
    if foundResult:
        break
