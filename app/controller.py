import sqlalchemy

from app.models.mysql.user import UserModel

from app.database.mysql import Base, engine
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)


class BaseController(object):
    """ Base View to create helpers common to all Webservices.
    """
    def __init__(self, db: Session, data: dict = {}):
        """
        Constructor
        """
        self.close_session = None
        if db:
            self.db = db
        else:
            self.db = Session(engine)
            self.close_session = True

        self.data = data
        self.model_class = None
       

    def get_all(self):
        """
        Method GET All
        """
        try:
            query = self.db.query(self.model_class).limit(100).all()
            return query

        except Exception as error:
            print(error)

        finally:
            if self.close_session:
                self.db.close()


class ControllerUser(BaseController):
    """
    Controller User
    """
    def __init__(self, db: Session, data: dict = {}):
        super().__init__(db, data)

        self.model_class = UserModel


class ControllerSyncUser(BaseController):
    """
    Controller SyncUser
    """
    def __init__(self, db: Session, data: dict = {}):
        super().__init__(db, data)

        self.model_class = UserModel

