filename = "Day8Input.txt"
textfile = open(filename, "r")
puzzle_input = textfile.read().split()
intInput = []

for x in puzzle_input:  # Parse all entries to integers
    intInput.append(int(x))


def parse(data):
    # Get the header information which is the number of child nodes and number of metadata entries
    children, metadataEntries = data[:2]
    # Get the rest of the input (the children)
    data = data[2:]
    scores = []  # The 'score' is total of the metadata of each child (including to the root node)
    totals = 0

    for i in range(children):
        total, score, data = parse(data)  # Recursively call parse method for each child node
        totals += total  # Increment the grand total with the total of each child node's data
        scores.append(score)

    totals += sum(data[:metadataEntries])

    if children == 0:  # If the node has no children, don't attempt to find the value of the root node
        return totals, sum(data[:metadataEntries]), data[metadataEntries:]
    else:  # If the node has children, find value to root node
        metadataSum = 0
        for value in data[:metadataEntries]:
            if value > 0 and value <= len(scores):  # Whilst the node has children
                metadataSum += scores[value - 1]

        return totals, metadataSum, data[metadataEntries:]


rootNode = parse(intInput)[1]

print(rootNode)
