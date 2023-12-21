# from main.database_set import database
# from main.model import *
#
# from main.model import users
#
#
# async def get_user(chat_id: int):
#     try:
#         query = users.select().where(users.c.chat_id==chat_id)
#         user = await database.fetch_one(query=query)
#         return user
#     except Exception as exc:
#         print(exc)
#         return False
#
# async def add_user(data: dict):
#     try:
#         query = users.insert().values(
#             full_name=data.get('full_name'),
#             phone_number=data.get('phone_number'),
#             language=('uz'),
#             chat_id=data.get('chat_id'),
#             created_at=data.get('created_at')
#         )
#         new_user = await database.execute(query=query)
#         return new_user
#     except Exception as exc:
#         print(exc)
#         return False
#
#
#
# async def add_test(message):
#     try:
#         query = tests.insert().values(
#             chat_id=message.chat.id,
#             title=message.chat.text,
#             created_at=message.date
#         )
#         new_test_id = await database.execute(query)
#         return new_test_id
#     except Exception as exc:
#         print(exc)
#         return None
#
#
#
# async def add_question(message,test_id):
#     try:
#         query = quesinis.insert().values(
#             test_id=test_id,
#             title=message.chat.text,
#             created_at=message.date
#         )
#         new_question_id = await database.execute(query)
#         return new_question_id
#     except Exception as exc:
#         print(exc)
#         return None
#
#
#
#
#
# async def add_cats(data: dict):
#     try:
#         query = cats.insert().values(
#             photo=data.get('photo'),
#             cat_name=data.get('cat_name'),
#             chat_id=data.get('chaat_id')
#         )
#
#         new_cat = await database.execute(query=query)
#         return new_cat
#     except Exception as exc:
#         print(exc)
#         return False
#
# async def get_my_cats(chat_id: int):
#     try:
#         query = cats.select().where(cats.c.chat_id==chat_id)
#         my_cats = await database.fetch_all(query)
#         return my_cats
#     except Exception as exc:
#         print(exc)
#         return False
#
# async def delete_cat(id: int):
#     try:
#         query = cats.delete().where(cats.c.id==id)
#         await database.execute(query=query)
#         return True
#     except Exception as exc:
#         print(exc)
#         return False