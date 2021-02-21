from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print ('This is a quiz game that tests your knowledge of Technology.')

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

end = False
while end == False:


            response= input("Would you like to play again?\n"
                         "If yes enter 'yes or 'y' if not enter'n' or 'no' to quit:\n")
            if response.lower()=="no" or response.lower()=="n":
                print("You have quit the game. Thank you for playing")
                keep_going = "end"
                break
            elif response.lower()=="yes" or response.lower()=="y":
                end = True
                print("Here is the Technology Quiz again")
                continue
            else:
                print("**Invalid input please enter 'y' if you want to play again\n or 'n' if you would like to quit game**\n")True