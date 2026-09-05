from Authentication.bases import Base
from sqlalchemy import Column,String,Integer

class Database(Base):
    __tablename__="database_model"
    
    id =  Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    username = Column(String,nullable=False)
    hash_password = Column(String,nullable=False)
    email = Column(String,nullable=False)