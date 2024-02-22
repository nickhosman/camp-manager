from typing import Optional

from sqlmodel import Field, SQLModel, create_engine

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_users():
    user_1 = User(username="Demo", email="demo@gmail.com", password="password")
    user_2 = User(username="nickhosman", email="nick@mail.co", password="password2")
    user_3 = User(username="test", email="test@mail.co", password="password3")
    user_4 = User(username="sarah", email="sarah@mail.co", password="password4")

if __name__ == "__main__":
    create_db_and_tables()
