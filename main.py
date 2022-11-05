from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create question bank which is list of objects from Question class
question_bank = []
for row in question_data:
    question = Question(row["text"], row["answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)
quiz_brain.start_game()
