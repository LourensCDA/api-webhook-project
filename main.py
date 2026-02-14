# def main():
#     print("Hello from api-webhook-project!")


# if __name__ == "__main__":
#     main()
from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship

engine = create_engine("sqlite:///database.db")


class Author(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    email: str = Field(default=None, max_length=255)
    books: list["Book"] = Relationship(back_populates="author")


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    author_id: int = Field(foreign_key="author.id")
    author: Author = Relationship(back_populates="books")


SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     author = Author(name="John Doe", email="john.doe@example.com")
#     session.add(author)
#     session.commit()
#     session.refresh(author)
#     book1 = Book(title="Book One", author_id=author.id)
#     book2 = Book(title="Book Two", author_id=author.id)
#     session.add_all([book1, book2])
#     session.commit()

with Session(engine) as session:
    statement = select(Author).where(Author.name == "John Doe")
    result = session.exec(statement)
    author = result.one()
    print(f"Author: {author.name}, Email: {author.email}")
    for book in author.books:
        print(f"Book: {book.title}")

    statement = select(Book)
    result = session.exec(statement)
    books = result.all()
    print("All Books:")
    for book in books:
        print(f"Book: {book.title}, Author ID: {book.author_id}")

    statement = select(Author).join(Book).where(Book.title == "Book One")
    result = session.exec(statement)
    author = result.one()
    print(f"Author of 'Book One': {author.name}")
