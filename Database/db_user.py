from sqlalchemy.orm.session import Session
from routers.schemas import UserBase
from Database.models import DbUser
from Database.hashing import Hash
from fastapi import HTTPException, status
 
def create_user(db: Session, request: UserBase):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    email = db.query(DbUser).filter(DbUser.email == request.email).first()
    
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Please Login user already exists')
    
    if email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already exists! Please use different email !')
    
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
    print("inside fn")
    user = db.query(DbUser).filter(DbUser.username == username).first()
    print("user ----------------------------------", user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with username {username} not found')
    return user