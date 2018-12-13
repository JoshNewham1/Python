filename = "Day8Input.txt"
textfile = open(filename, "r")
puzzle_input = textfile.read().split()
intInput = []

for x in puzzle_input:  # Parse all entries to integers
    intInput.append(int(x))


def parse(data):
    # Get the header information which is the number of child nodes and number of metadata entries
    children, metadata = data[:2]
    # Get the rest of the input (the children)
    data = data[2:]
    totals = 0

    for i in range(children):
        total, data = parse(data)  # Recursively call parse method for each child node
        totals += total  # Increment the grand total with the total of each child node's data

    totals += sum(data[:metadata])

    return totals, data[metadata:]


total = parse(intInput)[0]

print(total)
