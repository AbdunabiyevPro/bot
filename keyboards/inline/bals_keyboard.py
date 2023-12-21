from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


balls  =InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Top️🏈",callback_data="amerika"),
            InlineKeyboardButton(text="Voleybol🏐",callback_data="valibol"),
            InlineKeyboardButton(text="Futbol⚽️",callback_data="futbol")
        ],
        [
            InlineKeyboardButton(text="Golf🏑",callback_data="golf"),
            InlineKeyboardButton(text="Basketbol🏀",callback_data="baskitbol"),
            InlineKeyboardButton(text="Baseboll⚾️",callback_data="basebol"),
        ],
        [
            InlineKeyboardButton(text="Tennis🎾",callback_data="tennis"),
            InlineKeyboardButton(text="Bowling🎱",callback_data="bowling"),
            InlineKeyboardButton(text="Bagmington🏸",callback_data="bagminton")
        ],
        [
            InlineKeyboardButton(text="Back↩️",callback_data="back_main_menu")
        ]
    ]
)


bals=shop_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Buy✅",callback_data="buy"),
            InlineKeyboardButton(text="Add_Favorite⭐️",callback_data="favorite"),
        ],
        [
            InlineKeyboardButton(text="Back↩️",callback_data="back_top")
        ]
    ]
)



gym_shop = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Trunir",callback_data="turnir"),
            InlineKeyboardButton(text="Run",callback_data="run_trend"),
            InlineKeyboardButton(text="Kovrik",callback_data="Kovrik"),
        ],
        [
            InlineKeyboardButton(text="Gantel",callback_data="gantel"),
            InlineKeyboardButton(text="Arm Gantel",callback_data="arm"),
            InlineKeyboardButton(text="Jumpin",callback_data="jump")
        ],
        [
            InlineKeyboardButton(text="Back↩️",callback_data="back_main_menu")
        ]
    ]
)





check_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardMarkup(text="Kanalga a'zo bo'lish", url='https://t.me/+Q0NRDdZ89qowOGZi')
        ],
        [
            InlineKeyboardButton(text="Tekshirish", callback_data='check')
        ]
    ]
)