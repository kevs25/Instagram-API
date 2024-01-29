from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from Database.database import get_db
from routers.schemas import UserBase, UserDisplay
from Database import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.post('', response_model = UserDisplay)
def create_new_user(request : UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)