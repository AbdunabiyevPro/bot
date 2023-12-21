# import sqlalchemy
# from sqlalchemy import DateTime
# from main.database_set import metadata
#
# users = sqlalchemy.Table(
#     "users",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("full_name", sqlalchemy.String, nullable=True),
#     sqlalchemy.Column("language", sqlalchemy.String, nullable=True),
#     sqlalchemy.Column("chat_id", sqlalchemy.BigInteger),
#     sqlalchemy.Column("phone_number", sqlalchemy.String),
#     sqlalchemy.Column('created_at', DateTime(timezone=True), nullable=True)
# )
#
#
#
#
#
#
#
#
#
#
# cats = sqlalchemy.Table(
#     "cats",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
#     sqlalchemy.Column("chat_id", sqlalchemy.BigInteger),
#     sqlalchemy.Column("photo", sqlalchemy.String),
#     sqlalchemy.Column("cat_name", sqlalchemy.String, nullable=True)
# )