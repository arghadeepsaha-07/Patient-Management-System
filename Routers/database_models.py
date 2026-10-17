from sqlalchemy import Column,Integer,String,ForeignKey
from Authentication.bases import Base

class Patient_Database(Base):
    __tablename__ = "patients_database"

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,index=True,nullable=False)
    age = Column(Integer,nullable=False)
    gender = Column(String,nullable=False)
    height = Column(Integer,nullable=False)
    weight = Column(Integer,nullable=False)
    problem = Column(String,nullable=False)
    email = Column(String)
    phone_no = Column(String,nullable=False)
    emergency_phone_no = Column(String)
    
    
    user_id = Column(Integer, ForeignKey("database_model.id",ondelete="CASCADE"))
    
    '''
    What you cannot do

    This combination is invalid:

    id = Column(String, primary_key=True, autoincrement=True)

    because PostgreSQL's normal auto-increment mechanism generates numbers, while String expects text.
    
    '''
    '''
    Yes, if your application has users and each piece of CRUD data belongs to a user, it is important.

    This:

    user_id = Column(
        Integer,
        ForeignKey("authen_data.id", ondelete="CASCADE")
    )

    creates the relationship:

    Authen_data
    id = 1
        ↓
    User_Data
    user_id = 1
    Why is it important?

    1. It tells the database who owns the data.
        
    For example:

    Argha (user_id = 1)
    ├── Product A
    ├── Product B
    └── Product C

    Rahul (user_id = 2)
    ├── Product X
    └── Product Y

    Then you can query only Argha's data:

    db.query(User_Data).filter(User_Data.user_id == user.id).all()

    Without user_id, you can't reliably connect a CRUD record to its owner.

    2. ForeignKey protects your database.
    
    This:
    ForeignKey("authen_data.id")

    means user_id must refer to an existing user.

    3. ondelete="CASCADE" handles deletion.
    If user id=1 is deleted, their associated records can also be deleted automatically.
    Is ondelete="CASCADE" itself mandatory?

    No.
    You can have:

    user_id = Column(
        Integer,
        ForeignKey("authen_data.id")
    )

    and the foreign key still works.

    CASCADE is an additional behavior:

    "When the parent user is deleted, delete the related child records too."

'''
    