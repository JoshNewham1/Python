import statistics
# Simple averages program
# Variable declarations
finishedInput = False
validInput = False
total = 0
counter = 0
numberList=[]
# Start of program
print("Welcome to Averages")
typeOfAverage = input("Which average would you like to calculate? (Mean, Median, Mode or Range) ").lower()
if (typeOfAverage in ('median', 'mean', 'mode', 'range')):
    while (finishedInput == False):
        currentNum = input("Please enter a number: (Type 'Q' to quit) ")
        try:
            if (currentNum != 'Q'):
                int(currentNum)
        except ValueError:
            print("Please type a number or 'Q' to quit")
            continue
        else:
            # The user has inputted an integer
            if (typeOfAverage == "mean"):
                if (currentNum == "Q"):
                    print("Mean: " + str(total / counter))
                    finishedInput = True
                else:
                    total += int(currentNum)
                    counter += 1
            
            elif (typeOfAverage == "median"):
                if (currentNum == "Q"):
                    numberList.sort()
                    median = statistics.median(numberList)
                    print(median)
                    finishedInput = True
                else:
                    numberList.append(int(currentNum))
            elif (typeOfAverage == "mode"):
                if (currentNum == "Q"):
                    try:
                        numberList.sort()
                        mode = statistics.mode(numberList)
                    except statistics.StatisticsError:
                        print("There is no mode of these numbers")
                        break
                    print(mode)
                    finishedInput= True
                else:
                    numberList.append(currentNum)
            elif (typeOfAverage == "range"):
                if (currentNum == "Q"):
                    numberList.sort()
                    largestNum = int(numberList[len(numberList) - 1])
                    smallestNum = int(numberList[0])
                    range = largestNum - smallestNum
                    print(range)
                    finishedInput = True
                else:
                    numberList.append(currentNum)
else:
    print("Incorrect average type...")