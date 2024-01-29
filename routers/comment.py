from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from Database.database import get_db
from Database import db_comment
from routers.schemas import CommentBase, UserAuth
from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/comment',
    tags=['comment']
)

@router.get('/all/{post_id}')
def get_all_comments(post_id : int, db: Session = Depends(get_db)):
    return db_comment.get_all(db, post_id)


@router.post('')
def create(request: CommentBase, db: Session = Depends(get_db), current_user : UserAuth = Depends(get_current_user)):
    return db_comment.create(db, request)
    