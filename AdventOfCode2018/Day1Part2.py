filename = "Day1Input.txt"
frequency = 0
previous_frequencies = set() # Used 'set' data type to improve speed -> no indexing, faster
repeated_frequency = False

textfile = open(filename, "r")
puzzle_input = textfile.readlines()

while not repeated_frequency:
    for frequency_change in puzzle_input:
        previous_frequencies.add(frequency)
        change = frequency_change[0]
        number = int(frequency_change[1:])
        if change == "+":
            frequency += number
        elif change == "-":
            frequency -= number
        else:
            print("Error parsing string")
        if frequency in previous_frequencies and not repeated_frequency: # Looks up if the current frequency has occurred before
            print(frequency)
            repeated_frequency = True

print("Final frequency: " + str(frequency))
