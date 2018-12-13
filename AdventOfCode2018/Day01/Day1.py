filename = "Day1Input.txt"
frequency = 0

textfile = open(filename, "r")
puzzle_input = textfile.readlines()

for frequency_change in puzzle_input:
    change = frequency_change[0]
    number = int(frequency_change[1:])
    if change == "+":
        frequency += number
    elif change == "-":
        frequency -= number
    else:
        print("Error parsing string")

print(frequency)
