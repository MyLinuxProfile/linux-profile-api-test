from app.database.mysql import Base
from sqlalchemy import (
    Column,
    Integer,
    Unicode
)

class UserModel(Base):
    """Model User
    """
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user = Column(Unicode(50), nullable=False)
    email = Column(Unicode(100), nullable=False)
    token = Column(Unicode(255), nullable=False)

