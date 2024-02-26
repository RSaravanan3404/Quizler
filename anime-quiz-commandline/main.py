from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def attend_quiz():
    question_bank = []
    choice = []
    options = ""
    for movie in question_data:
        options += movie[0]+"/"
    series = input(f"Choose any Quiz.({options})").lower()
    for movie in question_data:
        if series == movie[0]:
            choice = movie[1]
    for question_text in choice:
        question = question_text["question"]
        answer = question_text["answer"]
        new_question = Question(question, answer)
        question_bank.append(new_question)
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    print("You've completed the quiz.")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")


yes = True
while yes:
    if input("Type yes to attend a new quiz. or Type no:") == "no":
        print("Thanks for visiting...")
        yes = False
    else:
        attend_quiz()
