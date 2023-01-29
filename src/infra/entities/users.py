"""User table"""

# pylint: disable=too-few-public-methods
from sqlalchemy import String, Column, Integer
from src.infra.config import Base


class User(Base):
    """User Entity"""

    __tablename__ = "user"

    id_user = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(50), nullable=False)

    def __rep__(self):
        return f"user name={self.name}"
