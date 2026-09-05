from pydantic import BaseModel,Field,ConfigDict

class Pydantic(BaseModel):
    name : str
    username : str
    password : str
    email : str
    
    
class Pydantic_Response(BaseModel):
    id :  int
    name : str
    username : str
    email : str
    
    model_config  = ConfigDict(from_attributes=True)
    
class Login_Schema(BaseModel):
    username : str
    password : str
    