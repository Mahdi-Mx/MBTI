from Load_files import questions
from state_management import TestState

def ask_questions():
    for question_id, question_data in questions.items():
        print(question_id,". ",question_data["text"], sep='')

