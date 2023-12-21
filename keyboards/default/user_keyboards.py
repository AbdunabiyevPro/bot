from aiogram.types import ReplyKeyboardMarkup, KeyboardButton





user_phone_share = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Send your phone number", request_contact=True)
        ]
    ], resize_keyboard=True
)


gym_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Balls⚽️"),
            KeyboardButton(text="GYM🏋️‍♀️"),
        ],
        [
            KeyboardButton(text="Boks🥊"),
            KeyboardButton(text="Swim🏊🏼‍♂️"),
        ],
        [
            KeyboardButton(text="Bike🚴‍♂️"),
            KeyboardButton(text="Prize🏆"),
        ],
        [
            KeyboardButton(text="Back")
        ]
    ], resize_keyboard=True
)


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Products🛍"),
            KeyboardButton(text="Favorites⭐️"),
        ],
        [
            KeyboardButton(text="Your order🛒"),
            KeyboardButton(text="Contact📞")
        ]
    ],resize_keyboard=True
)




