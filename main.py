import random
import operator

class IncorrectFormat(Exception):
    pass

def generate_simple_op(range):
    numbers = [num for num in range]
    operator_list = ['+', '-', '*']
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    num_1 = random.choice(numbers)
    num_2 = random.choice(numbers)
    operation = random.choice(operator_list)
    result = operators[operation](num_1, num_2)
    problem = f"{num_1} {operation} {num_2}"
    return problem, result

def generate_square_op(range):
    numbers = [num for num in range]
    num_1 = random.choice(numbers)
    result = pow(num_1, 2)
    problem = f"{num_1}"
    return problem, result

def check_result(problem, result):
    points = 0
    while True:
        try:
            answer = int(input(problem))
            if answer == result:
                print("Right!")
                points += 1
                break
            else:
                print("Wrong!")
                break
        except ValueError:
            print("Wrong format! Try again.")
    return points


score = 0
message = """Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
"""

while True:
    try:
        choice = int(input(message))
        if choice not in range(1, 3):
            raise IncorrectFormat
        break
    except (ValueError, IncorrectFormat):
        print("Incorrect format.")

if choice == 1:
    level = "level 1 - simple operations with numbers 2-9"
    for question in range(5):
        problem, result = generate_simple_op(range(2, 10))
        score += check_result(problem, result)
elif choice == 2:
    level = "level 2 - integral squares of 11-29"
    for question in range(5):
        problem, result = generate_square_op(range(11, 30))
        score += check_result(problem, result)


save = input(f"Your mark is {score}/5. Would you like to save your result to the file? Enter yes or no.")
if save in ('yes', 'YES', 'y', 'Yes'):
    name = input("What is your name?")
    saved = open('results.txt', 'a', encoding='utf-8')
    saved.write(f"{name}: {score}/5 in {level}")
    saved.close()
    print('The results are saved in "results.txt".')
else:
    exit()