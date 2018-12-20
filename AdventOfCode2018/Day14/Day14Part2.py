inputRecipes = 306281  # Puzzle input
scoreboard = '37'  # Scores 3 and 7 already on leaderboard
elf1 = 0  # Elf 1 starting score from problem
elf2 = 1  # Elf 2 starting score from problem

# Whilst the desired recipe string hasn't been reached
while str(inputRecipes) not in scoreboard[-7:]:
    # Calculate the total of both elf's scores
    total = int(scoreboard[elf1]) + int(scoreboard[elf2])
    # Concatenate it to the scoreboard
    scoreboard += str(total)
    # Calculate the scores of the elves by adding current to new score,
    # adding 1 and shorten it to the appropriate size using modulus
    elf1 = (elf1 + int(scoreboard[elf1]) + 1) % len(scoreboard)
    elf2 = (elf2 + int(scoreboard[elf2]) + 1) % len(scoreboard)

# Part 2 requires num of recipes to the left of desired recipes
# Can simply use scoreboard.index() to find index of desired
print(scoreboard.index(str(inputRecipes)))
