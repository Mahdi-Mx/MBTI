from enum import Enum, auto
from ui import start_testing
from QandA import introduce_MBTI

class TestState(Enum):
    START = auto()
    QandA = auto()
    ASKING_QUESTION = auto()
    CALCULATING = auto()
    RESULT = auto()
    FINISHED = auto()


async def state_conditions(current_state: str):
    if current_state == TestState.START:
        await start_testing()
    elif current_state == TestState.QandA:
        await introduce_MBTI()
    