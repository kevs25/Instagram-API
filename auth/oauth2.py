from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWEError
from fastapi import Depends, status
from sqlalchemy.orm import Session
from fastapi import HTTPException
from Database.database import get_db
from Database import db_user

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login') #This parameter contains the URL that the client (the frontend running in the user's browser) will use to send the username and password in order to get a token.

 
SECRET_KEY = '0315c54bb643747d0d4260b604d75de50a946e26dd8aa728184712977ccdc4bb'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  print("encoded_jwt", encoded_jwt)
  return encoded_jwt


def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    Credentials_exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Could not validate credentials',
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("payload----", payload)
        username: str = payload.get("username") #retrive username from token
        if username is None:
            raise Credentials_exception
    
    except JWEError:
        raise Credentials_exception
    
    print(username)
    user = db_user.get_user_by_username(db, username=username)
    
    if user is None:
        raise Credentials_exception
    
    return user        