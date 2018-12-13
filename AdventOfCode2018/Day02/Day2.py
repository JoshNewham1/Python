import collections

repeatedTwo = 0
repeatedThree = 0

filename = "Day2Input.txt"
textfile = open(filename, "r")
puzzle_input = textfile.readlines()

repeated_chars = collections.defaultdict(int) # Using defaultdict (will insert if item doesn't exist)

for items in puzzle_input: # Loop through all the input
    foundTwo = False # Each list of items can only have one set of two duplicates
    foundThree = False # Each list of items can only have one set of three duplicates
    for char in items:
        repeated_chars[char] += 1
    for char in sorted(repeated_chars, key=repeated_chars.get, reverse=True): # Loop through dictionary and sort it
        if repeated_chars[char] == 2 and not foundTwo: # If character has been repeated two times
            repeatedTwo += 1
            foundTwo = True
        elif repeated_chars[char] == 3 and not foundThree: # If the letter has been repeated three times
            repeatedThree += 1
            foundThree = True
    repeated_chars.clear() # Clear the dictionary after each list of items

checksum = repeatedTwo * repeatedThree # Calculate the 'checksum'
print(checksum)