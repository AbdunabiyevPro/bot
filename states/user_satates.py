from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    full_name = State()
    phone_number = State()



class QuestionCreateState(StatesGroup):
    question_title = State()
    answer_title = State()
    is_true = State()
    next_step = State()




class TestState(StatesGroup):
    test_name = State()
    question = State()
    option = State()




class CatsState(StatesGroup):
    name = State()
    photo = State()