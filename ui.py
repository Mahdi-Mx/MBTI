from state_management import TestState, state_conditions
from ask_questions import ask_questions

def start_testing():
    text = """
Choose one of them:
1. Start testing
2. Q&A
3. Exit
> """
    while True:
        try:
            chosen = int(input(text))
            if chosen == 1:
                state_conditions(TestState.START)
            elif chosen == 2:
                state_conditions(TestState.QandA)
            elif chosen == 3:
                break
        except ValueError:
            print("Invalid input. try again!")




def main():
    start_testing()

if __name__ == "__main__":
    main()