import random

q_a_list = [
    ["Grass", "green", "yellow", "red"],
    ["icon for twitter", "bird", "house", "large blue f"],


]

question_answer = random.choice(q_a_list)
print(question_answer)

question = question_answer[0]
answer = question_answer[1]
other_answers = question_answer[2:]

print(question)
print(answer, other_answers)