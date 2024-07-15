from sqlalchemy.ext. declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String)
    reset_token = Column(String)

    def __repr__(self):
        return f'<User {self.id}, {self.email}, {self.hashed_password}, {self.session_id}, {self.reset_token}>'