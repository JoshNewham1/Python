def loadinput(filename):
    # Read the text file into an array
    with open(filename, "r") as file:
        lines = file.readlines()
    # Concatenate three empty pots to the start and end of the initial state
    # so the plants have space to grow in both directions
    state = "..." + lines[0].split()[2] + "..."
    # Load in only the rules that result in growth (other ones redundant)
    rules = {line[:5] for line in lines[2:] if line.rstrip()[-1] == "#"}

    # Return the dictionary of rules, the initial state and the index of the first, non-negative plant
    # which is now 3 due to the concatenation
    return rules, state, 3


def evolve(generations):
    rules, state, centreIndex = loadinput("Day12Input.txt")
    for generation in range(1, generations + 1):  # Loop through every generation
        newState = ["."] * len(state)  # Create an array of empty pots
        for index in range(2, len(state) - 2):  # Loop over previous state (starting at 2 so 5 chars can be taken)
            if state[(index-2):(index+3)] in rules:  # If the five char section conforms to a rule
                newState[index] = "#"  # 'Grow' a plant
        state = "".join(newState)  # When done, join new 'evolution' back to the state
        if state[0:3] != "...":  # If a plant has grown at the start of the state
            centreIndex += 3  # Update the centre index accordingly
            state = "..." + state  # Concatenate three empty pots to the beginning
        if state[-3:] != "...":  # If a plant has grown at the end of the state
            state = state + "..."  # Concatenate three empty pots to the end

    total = 0
    for position, char in enumerate(state):
        if char == "#":
            total += (position - centreIndex)
    return total


print(evolve(20))