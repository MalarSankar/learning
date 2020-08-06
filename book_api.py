from flask import *
from sqlalchemy import  create_engine

app = Flask(__name__)
app.config['DEBUG']=True
def db_connection():
    DATABASE_URL = "postgresql://postgres:7538821247@localhost:5432/flask"
    return create_engine(DATABASE_URL)


@app.route('/', methods=['GET'])
def get_all_books():
    book = db.execute("select * from bookstall.book;")
    formated_result = [dict(row) for row in book]
    return jsonify(formated_result)


@app.route('/insert', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_name = request.form['book_name']
        author_name = request.form['author_name']
        db.execute("INSERT INTO bookstall.book(book_name,author_name) VALUES('{}','{}');".format(book_name,author_name))
        return 'Book added successfully'


db=db_connection()
app.run()