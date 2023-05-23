import csv
import datetime

from flask import Flask, jsonify, request
from sqlalchemy import Column, INTEGER, String, DATE, FLOAT, BOOLEAN, DATETIME, create_engine, and_, ForeignKey, func
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, backref

engine = create_engine("sqlite:///library.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
app = Flask(__name__)


# region ORM
class Book(Base):
    __tablename__ = "books"
    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(INTEGER, default=1)
    release_date = Column(DATE, nullable=False)
    author_id = Column(INTEGER, ForeignKey('authors.id'), nullable=False)

    author = relationship("Author", backref=backref("books", cascade="all, " "delete-orphan", lazy="joined"))

    receiving_books = relationship("ReceivingBooks", back_populates="book", cascade="all, " "delete-orphan",
                                   lazy="joined")
    students = association_proxy("receiving_books", "student")

    def __init__(self, name, release_date, count, author_id):
        self.author_id = author_id
        self.release_date = release_date
        self.name = name
        self.count = count

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = "authors"
    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = "students"
    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    average_score = Column(FLOAT, nullable=False)
    scholarship = Column(BOOLEAN, nullable=False)

    receiving_books = relationship("ReceivingBooks", back_populates="student", cascade="all, " "delete-orphan",
                                   lazy="joined")
    books = association_proxy("receiving_books", "book")

    def __init__(self, name, surname, phone, email, average_score, scholarship):
        self.average_score = average_score
        self.email = email
        self.phone = phone
        self.surname = surname
        self.name = name
        self.scholarship = scholarship

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_scholarship_students(cls):
        return session.query(Student).filter(Student.scholarship).all()

    @classmethod
    def get_students_by_score_higher_then(cls, score):
        return session.query(Student).filter(Student.average_score > score).all()


class ReceivingBooks(Base):
    __tablename__ = "receiving_books"
    id = Column(INTEGER, primary_key=True)
    book_id = Column(INTEGER, ForeignKey('books.id'), primary_key=True)
    student_id = Column(INTEGER, ForeignKey('students.id'), primary_key=True)
    date_of_issue = Column(DATETIME, nullable=False)
    date_of_return = Column(DATETIME)

    student = relationship("Student", back_populates="receiving_books")
    book = relationship("Book", back_populates="receiving_books")

    def __init__(self, book_id, student_id, date_of_issue, date_of_return):
        self.date_of_issue = date_of_issue
        self.date_of_return = date_of_return
        self.student_id = student_id
        self.book_id = book_id

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return:
            return (self.date_of_return - self.date_of_issue).days, 'Книга сдана'
        else:
            return (datetime.datetime.now() - self.date_of_issue).days, 'Книга у читателя'


# endregion


# region Route
@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route('/get_books/', methods=["GET"])
def get_books():
    books_list = []
    for book in session.query(Book).all():
        books_list.append(book.to_json())

    return jsonify(books_list=books_list), 200


@app.route('/get_books_by_name/<string:name>/', methods=["GET"])
def get_books_by_name(name):
    books_list = []
    for book in session.query(Book).filter(Book.name.like(f"%{name}%")).all():
        books_list.append(book.to_json())
    return jsonify(books_list=books_list), 200


@app.route('/get_count_of_remaining_books_by_author/<int:author_id>/', methods=["GET"])
def get_count_of_remaining_books_by_author(author_id):
    books_count = session.query(func.sum(Book.count)).filter(Book.author_id == author_id).scalar()
    return str(books_count), 200


@app.route('/get_not_read_books_by_student/<int:student_id>/', methods=["GET"])
def get_not_read_books_by_student(student_id):
    student = session.query(Student).filter(Student.id == student_id).scalar()
    books = map(lambda book: book.id, student.books)
    authors = session.query(Author).subquery()
    books_not_read = [book.to_json() for book in session.query(Book) \
        .join(authors, Book.author_id == authors.columns.id) \
        .group_by(authors.columns.id) \
        .filter(Book.id.not_in(books)).all()]
    return jsonify(books_not_read=books_not_read), 200


@app.route('/get_average_number_book_having_students_this_months/', methods=["GET"])
def get_average_number_book_having_students_this_months():
    count_books_by_student = session.query(ReceivingBooks.book_id) \
        .group_by(ReceivingBooks.student_id) \
        .filter(func.extract('month', ReceivingBooks.date_of_issue) == datetime.datetime.now().month).subquery()
    books_count_avg = session.query(func.avg(count_books_by_student)).scalar()
    return str(books_count_avg), 200


@app.route('/get_most_popular_book_among_students_with_high_gpa/', methods=["GET"])
def get_most_popular_book_among_students_with_high_gpa():
    gpa: float = 4.0
    books_count = session.query(Book.name.label("book"), func.count(ReceivingBooks.student_id).label("count")) \
        .group_by(ReceivingBooks.book_id) \
        .filter(Book.id == ReceivingBooks.book_id, Student.id == ReceivingBooks.student_id, Student.average_score > gpa) \
        .subquery()

    most_popular_book: str = session.query(books_count.columns.book, func.max(books_count.columns.count)).scalar()
    return most_popular_book, 200


@app.route('/get_most_reading_student_this_year/', methods=["GET"])
def get_most_reading_student_this_year():
    top_students = session.query(Student.name, Student.surname) \
        .group_by(ReceivingBooks.student_id) \
        .filter(Student.id == ReceivingBooks.student_id) \
        .order_by(func.count(ReceivingBooks.book_id).desc()) \
        .limit(10) \
        .all()

    return str(top_students), 200


@app.route('/set_students/', methods=["POST"])
def set_student():
    students_data = request.files["students"]
    with open(students_data.filename, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        students = [{"name": row["name"],
                     "surname": row["surname"],
                     "phone": row["phone"],
                     "email": row["email"],
                     "average_score": float(row["average_score"]),
                     "scholarship": float(row["scholarship"])} for row in reader]

        session.bulk_insert_mappings(Student, students)
        session.commit()
    return "OK", 200


@app.route('/get_debtors/', methods=["GET"])
def get_debtors():
    debtors_list = []
    for receiving_book in session.query(ReceivingBooks).filter(ReceivingBooks.date_of_return == None).all():
        if receiving_book.count_date_with_book[0] > 14:
            debtors_list.append(receiving_book.to_json())

    return jsonify(debtors_list=debtors_list), 200


@app.route('/issue_book/', methods=["POST"])
def issue_book():
    book_id = request.form.get('book_id')
    student_id = request.form.get('student_id')
    session.add(ReceivingBooks(book_id=book_id, student_id=student_id, date_of_issue=datetime.datetime.now()))
    book = session.query(Book).get(book_id)
    book.count = book.count - 1
    session.commit()

    return f"Книга {book_id} успешно выдана студенту {student_id}"


@app.route('/pass_book/', methods=["POST"])
def pass_book():
    book_id = request.form.get('book_id')
    student_id = request.form.get('student_id')
    receiving_book = session.query(ReceivingBooks).filter(and_(ReceivingBooks.student_id == student_id,
                                                               ReceivingBooks.book_id == book_id,
                                                               ReceivingBooks.date_of_return == None)).one_or_none()
    if receiving_book:
        receiving_book.date_of_return = datetime.datetime.now()
        book = session.query(Book).get(book_id)
        book.count = book.count + 1
        session.commit()
        return f"Книга {book_id} сдана"
    else:
        return f"Связка книги({book_id}) и студента({student_id})не найдена"


# endregion


if __name__ == '__main__':
    app.run(debug=True)
