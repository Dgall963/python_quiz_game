from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def displayIntro():
    print('Hello. and Welcome to the game! What is your name?')
myname = input()
print ('Well, ' +myname + ' This is a quiz game that tests your knowledge of Technology.')

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)
        
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
print('Do you want to play again? (yes or no)')
playagain = 'yes'
while playagain == 'yes': 
    displayIntro()
    playAgain = input()