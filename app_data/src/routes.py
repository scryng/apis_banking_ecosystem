from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database import get_session
from src.models import User
from src.schemas import UserList, UserPublic, UserSchema

router = APIRouter()


@router.post(
    '/users', status_code=HTTPStatus.CREATED, response_model=UserPublic
)
def create_user(user: UserSchema, session=Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Username already exists',
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail='Email already exists',
            )

    db_user = User(
        username=user.username, email=user.email, password=user.password
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.get('/users', response_model=UserList)
def read_users(
    limit: int = 10, offset: int = 0, session: Session = Depends(get_session)
):
    user = session.scalars(select(User).limit(limit).offset(offset))

    return {'users': user}
