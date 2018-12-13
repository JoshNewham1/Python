# Needs a complete rewrite from Part 1
# As multiple steps can be processed simultaneously
from collections import defaultdict

puzzle_input = open("Day7Input.txt")

numberWorkers = 5
dependencies = defaultdict(list)
steps = set()
done = []
steptimes = {}

for line in puzzle_input:
    x = line[5]
    y = line[36]
    dependencies[y].append(x)
    steps.add(x)
    steps.add(y)

# Find steps without dependencies
startingPoint = ord('A')
for step in sorted(steps):
    steptimes[step] = ord(step) - startingPoint + 61
    if step not in dependencies:  # If the step doesn't have any dependencies
        dependencies[step] = []  # Add it to the dependencies dictionary

currentSecond = 0
# Loop through the list of steps and their dependencies,
# removing the first one with all its dependencies complete (alphabetically)
while len(dependencies) > 0:  # While all dependencies haven't been satisfied
    possible = []
    for step in dependencies.items():  # Loop through all steps
        ready = True
        for dependency in step[1]:  # Loops through dependencies of the steps
            if dependency not in done:  # If the dependency hasn't been satisfied
                ready = False
        if ready:  # If the dependency has been satisfied
            possible.append(step[0])  # Add the step to the possible list

    possible = sorted(possible)  # Sort the possible list alphabetically
    for i in range(min(numberWorkers, len(possible))):  # Loop through each worker
        steptimes[possible[i]] -= 1  # Decrement one second from their time

    for item in possible:
        if steptimes[item] < 1:  # If the worker has completed the step
            done += item  # Add to the done list
            del dependencies[item]  # Delete from the dependencies list

    currentSecond += 1  # Increment the current second

print("".join(done))

print(currentSecond)
