# https://www.udemy.com/course/100-days-of-code/learn/lecture/19964886#overview

# Day 17

# Quiz project
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# i = 0
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))
    # print(question_bank[i].text)
    # i += 1

quiz = QuizBrain(question_bank)
#print(len(question_bank))
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{len(question_bank)}.")