# code from https://stackoverflow.com/questions/24662571/python-import-csv-to-list
import csv
import random


class ColourIt:

        def __init__(self, red, green, blue, text):
                self.red = red
                self.green = green
                self.blue = blue
                self.text = text

        def get_color_escape(self, red, green, blue):
                return '\033[{};2;{};{};{}m'.format(38, red, green, blue)

        def print_colour(self):
                # the bit at the end resets the colour back to normal
                all_coloured = self.get_color_escape(self.red, self.green, self.blue) + self.text + '\033[0;0m'
                return all_coloured

def instructions():
    print()
    print(colour_green("**** How to Play****"))
    print()
    print(colour_gray("A question will appear on screen with 4 possible answers."))
    print(colour_gray("Each answer will be numbered 1 to 4."))
    print(colour_gray("Type in the number next to the answer you think is correct."))
    print(colour_yellow("\nEnjoy!\n"))
    return""

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print(colour_red("Please answer yes / no\n"))
            
            
def num_check(question, low, high):
    error = "\nPlease enter a whole number between 1 and 4\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if low < response <= high:
                return response
            # output an error
            else:
                print(colour_red(error))
        except ValueError:
            print(colour_red(error))

def previous_player():
    print()
    return yes_no(colour_yellow("Have you played before? "))
    

def colour_green(message):    
    return ColourIt(69, 242, 34, message).print_colour()


def colour_red(message):
    return ColourIt(209, 71, 61, message).print_colour()


def colour_yellow(message):
    return ColourIt(191, 194, 54, message).print_colour()


def colour_gray(message):
    return ColourIt(130, 130, 130, message).print_colour()


def colour_blue(message):
    return ColourIt(34, 34, 242, message).print_colour()


def colour_aqua(message):
    return ColourIt(34, 242, 193, message).print_colour()


def colour_orange(message):
    return ColourIt(255, 162, 23, message).print_colour()

with open('04_Trivia_quiz\Questions.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

played_before = (previous_player())

rounds_played = 0
rounds_won = 0
rounds_lost = 0
used_questions = []

if played_before == "no":
   instructions()
elif played_before == "yes":
    print()

play_again = "yes"
while play_again == "yes":
    # Choose randomly from the list

    question_answers = random.choice(data)

    # Saves answer and question

    question = question_answers[1]
    correct_ans = question_answers[2]
    
    if question in used_questions:
        continue
    
    else:
        rounds_played += 1
        used_questions.append(question)
        # Print question
        print(colour_blue("Question Number {}".format(rounds_played)))
        print(colour_green(question))

        # Shuffles answers

        print(colour_aqua("possible answers..."))

        possible_ans = question_answers[2:]
        random.shuffle(possible_ans)

        for item in possible_ans:
            choice = "{}. {}".format(possible_ans.index(item)+1, item)
            print(colour_gray(choice))

        guess = num_check("Your guess is: ", 0, 4)

        if possible_ans[guess - 1] == correct_ans: 
            rounds_won += 1
            print(colour_green("That was correct!!"))
        else: 
            rounds_lost += 1
            print(colour_red("Incorrect!"))
            print(colour_yellow("Correct Answer was {}".format(correct_ans)))
        if rounds_played == 80:
            print(colour_orange("\nYou've answered all the questions!\n"))
            break
        else:
            play_again = yes_no("Would you like to do another question (yes / no)? ") 
            print() 
   

print(colour_green("Thanks for playing!"))
print(colour_orange("You answered {} incorrectly".format(rounds_lost)))
print(colour_orange("Overall you answered a total of {}/{} correctly".format(rounds_won, rounds_played)))