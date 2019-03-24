import random
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux
    else:
        system('clear')


print("GCSE AQA Maths Trig Values Test")
print("You will be tested on all trig values needed for Paper 1")
print("Please set out your answers like this: root(1)/1")
print("Or 'impossible' if the value cannot be calculated")
print("Answers will only be accepted in their simplest form")
values = [0, 30, 45, 60, 90]
completed = list()
answers = {'1:0': '0', '1:30': '1/2', '1:45': 'root(2)/2', '1:60': 'root(3)/2', '1:90': '1',
           '2:0': '1', '2:30': 'root(3)/2', '2:45': 'root(2)/2', '2:60': '1/2', '2:90': '0',
           '3:0': '0', '3:30': 'root(3)/3', '3:45': '1', '3:60': 'root(3)', '3:90': 'impossible'}

while len(completed) != 14:
    operator = random.randint(1, 3)  # Randomises for either sin (1), cos (2) or tan (3)
    number = values[random.randint(0, 4)]
    dict_set = str(operator) + ':' + str(number)
    if dict_set not in completed:
        if operator == 1:
            user_answer = input("Sin" + str(number) + ": ")
            correct_answer = answers[dict_set]
            if user_answer.strip() == correct_answer:
                print("Correct")
                completed.append(dict_set)
            else:
                print("Incorrect")
                print("Correct answer was " + correct_answer)
            input('')
            clear()
        elif operator == 2:
            user_answer = input("Cos" + str(number) + ": ")
            correct_answer = answers[dict_set]
            if user_answer.strip() == correct_answer:
                print("Correct")
                completed.append(dict_set)
            else:
                print("Incorrect")
                print("Correct answer was " + correct_answer)
            input('')
            clear()
        elif operator == 3:
            if dict_set == '3:30':
                print("NOTE: This one requires further simplification from the output of the 'finger method'")
            user_answer = input("Tan" + str(number) + ": ")
            correct_answer = answers[dict_set]
            if user_answer.strip() == correct_answer:
                print("Correct")
                completed.append(dict_set)
            else:
                print("Incorrect")
                print("Correct answer was " + correct_answer)
            input('')
            clear()

print("Completed")
