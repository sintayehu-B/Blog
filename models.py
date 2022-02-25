from sqlalchemy.sql import text
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
# from settings import engine
from sqlalchemy import inspect

metadata = MetaData()
book = Table('Books', metadata,
             Column('isbn', String, primary_key=True,
                    nullable=False, autoincrement=False),
             Column('title', String, nullable=False),
             Column('primary_author', String, nullable=False),
             Column('year', Integer, nullable=False),
             )

review = Table('Reviews', metadata,
               Column('user_id', Integer, ForeignKey("Users.id"),
                      primary_key=True, nullable=False),
               Column('isbn', String, ForeignKey("Books.isbn"),
                      primary_key=True,  nullable=False),
               Column('review', String, nullable=False),
               )

ratings = Table('Ratings', metadata,
                Column('user_id', Integer, ForeignKey("Users.id"),
                       primary_key=True, nullable=False),
                Column('isbn', String, ForeignKey("Books.isbn"),
                       primary_key=True, nullable=False),
                Column('rating', Integer, nullable=False),
                )

users = Table('Users', metadata,
              Column('id', Integer, primary_key=True, nullable=False),
              Column('username', String, nullable=False, unique=True),
              Column('email', String, nullable=False, unique=True),
              Column('fullname', String, nullable=False),
              Column('password', String, nullable=False, unique=True),
              )

registeredYetNotVerified = Table('RegisteredYetNotVerified', metadata,
                                 Column('id', Integer, primary_key=True,
                                        nullable=False),
                                 Column('username', String,
                                        nullable=False, unique=True),
                                 Column('email', String,
                                        nullable=False, unique=True),
                                 Column('fullname', String, nullable=False),
                                 Column('password', String,
                                        nullable=False, unique=True),
                                 Column('registrationcode', Integer,
                                        unique=True, nullable=False),
                                 )


# engine = create_engine(
#     'postgresql://vnydofzsfucois:9c027b5996732361dc5c84fa6ba5d76345248a5b90c596fe322c63f493b84e8b@ec2-54-90-211-192.compute-1.amazonaws.com:5432/d7likgvnep5q8i')
metadata.create_all(engine)

# inspector = inspect(engine)

# print(metadata.tables.keys())

# le = inspector.get_columns('Books')
# for i in le:
#      print(i)
# print("--------------------------------------------------------------------------------------------")
# l2 = inspector.get_columns('Reviews')
# for j in l2:
#     print(j)
# print("--------------------------------------------------------------------------------------------")
# leq = inspector.get_columns('Ratings')
# for k in leq:
#     print(k)
# print("--------------------------------------------------------------------------------------------")
# lek = inspector.get_columns('Users')
# for l in lek:
#     print(l)
# print("--------------------------------------------------------------------------------------------")
# lew = inspector.get_columns('RegisteredYetNotVerified')
# for n in lew:
#     print(n)


# with engine.connect() as con:

#     data = ( { "id": 3, "title": "The Hobbit", "primary_author": "Tolkien" },
#              { "id": 4, "title": "The Silmarillion", "primary_author": "Tolkien" },
#     )

#     statement = text("""INSERT INTO book(id, title, primary_author) VALUES(:id, :title, :primary_author)""")

#     # for line in data:
#         # con.execute(statement, **line)
#     sat = text("""SELECT * FROM "Books" WHERE "isbn" LIKE '055356073%' """)
#     print(con.execute(sat).all())
#     j = 0
#     rs = con.execute('SELECT * FROM "Books"')
#     for row in rs:
#         print(row)
#         j += 1
#     print(j)

#     con.execute('DROP TABLE "Reviews"')
#     con.execute('DROP TABLE "Ratings"')
#     con.execute('DROP TABLE "Users"')
#     con.execute('DROP TABLE "RegisteredYetNotVerified"')
#     con.execute('DROP TABLE "Books"')
