i = 0
numOfSquares = input("How many squares would you like to output? ")
try:
    int(numOfSquares)
except ValueError:
    print("Please type a valid number...")
    quit()
for i in range(1, int(numOfSquares) + 1):
    print(str(i) + " squared is " + str(i ** 2))