from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserBase(BaseModel):
    username : str
    email : str
    password :  str

class UserDisplay(BaseModel):
    username : str
    email : str
    class config():
        orm_mode = True
        
#send information to api
class PostBase(BaseModel):
    image_url : str
    image_url_type : str
    caption : str
    creator_id : int
    
#for post display
class User(BaseModel):
    username: str
    class config():
        orm_mode = True
        
class Comment(BaseModel):
    text : str
    username : str
    timestamp : datetime
    class config():
        orm_mode = True  

#display to user
class PostDisplay(BaseModel):
    id : int
    image_url : str
    image_url_type : str
    caption : str
    timestamp : datetime
    user: User
    comments : List[Comment]
    class config():
        orm_mode = True
        
class UserAuth(BaseModel):
    id : int
    username : str
    email : str
    
class CommentBase(BaseModel):
    username : str
    text : str
    post_id : int
    