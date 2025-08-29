from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandlerS:
    def __init__(self) -> None:
        my_password = "Root1-password"
        self.__connection_string = f'mysql+pymysql://root:{my_password}@localhost:3306/dental_app' 
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()