from app.models.mysql.user import UserModel
from app.models.mysql.sync_profile import SyncUserModel
from app.database.mysql import Base, engine

from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)


class BaseController(object):
    """ Base View to create helpers common to all Webservices.
    """
    def __init__(self, db: Session, user_id: int, data: dict = {}):
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
        self.user_id = user_id
        self.model_class = None
       
    def get_all(self):
        """Method GET All
        """
        try:
            query = self.db.query(self.model_class).filter(
                self.model_class.user_id == self.user_id
            ).all()
            return query

        except Exception as error:
            print(error)

        finally:
            if self.close_session:
                self.db.close()

    def get(self, model_id: int):
        """Method GET
        """
        try:
            query = self.db.query(self.model_class) \
                .filter(
                    self.model_class.user_id,
                    self.model_class.id == model_id).first()
            return query

        except Exception as error:
            print(error)

        finally:
            if self.close_session:
                self.db.close()


class ControllerUser(BaseController):
    """Controller User
    """
    def __init__(self, db: Session, data: dict = {}, user_id: int = None):
        super().__init__(db, user_id, data)

        self.model_class = UserModel

    def get_token(self, email: str, token: str):
        """GET Token
        """
        try:
            query = self.db.query(self.model_class) \
                .filter(
                    self.model_class.email == email,
                    self.model_class.token == token
                ).first()

            return query

        except Exception as error:
            print(error)

        finally:
            self.db.close()


class ControllerSyncUser(BaseController):
    """Controller SyncUser
    """
    def __init__(self, db: Session, user_id: int, data: dict = {}):
        super().__init__(db, user_id, data)

        self.model_class = SyncUserModel
