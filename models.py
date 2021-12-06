import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

engine = sqlalchemy.create_engine("mariadb+mariadbconnector://csc2033_team27:Lobe?CamJest!@cs-db.ncl.ac.uk:3306/csc2033_team27")
Base = declarative_base()


def init_db():
    Base.metadata.create_all(engine)



