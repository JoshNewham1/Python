filename = "Day7Input.txt"
textfile = open(filename, "r")
puzzle_input = textfile.readlines()
steps = {}

for line in puzzle_input:
    dependent = line[5]
    resulting = line[36]

    # Gathers all steps in dict and groups them by their required steps
    # e.g. T: [L, A ...]
    if resulting not in steps:
        steps[resulting] = []
    if dependent not in steps:
        steps[dependent] = []
    steps[resulting].append(dependent)

result = ""
while len(steps):  # Carries out all steps (deletes them from steps dictionary and adds them to end result)
    currentStep = sorted(k for k, v in steps.items() if len(v) == 0)[0]
    del steps[currentStep]
    for key in steps:
        if currentStep in steps[key]:
            steps[key].remove(currentStep)
    result += currentStep
print(result)
