import csv
# import sqlalchemy
from sqlalchemy.sql import text
from sqlalchemy import create_engine, insert
from settings import engine
from models import *

with open('books.csv', 'r') as books_csv:
    book_csv_reader = csv.reader(books_csv)
print(book_csv_reader)
    next(book_csv_reader)
    for b in book_csv_reader:
        book = {'isbn': b[0], 'title': b[1],
                'primary_author': b[2], 'year': b[3]}

        with engine.connect() as conn:
            statement = text(
                """INSERT INTO "Books"(isbn, title, primary_author, year) VALUES(:isbn, :title, :primary_author, :year)""")
            conn.execute(statement, **book)
