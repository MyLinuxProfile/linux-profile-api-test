from app.database.mysql import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)

class SyncUserModel(Base):
    """
    Model Sync User
    """
    __tablename__ = 'sync_user'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    profile_id = Column(String(100), index=True)

