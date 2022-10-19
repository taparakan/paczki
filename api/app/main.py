from fastapi import FastAPI, Depends, HTTPException, Request, status
from .db import engine
from sqlmodel import Field, SQLModel, select, Session

from . import models
import os
import random
import string
import time

from authlib.integrations.starlette_client import OAuth, OAuthError
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse

SQLModel.metadata.create_all(engine)

app = FastAPI()

session = Session(bind=engine)


@app.get('/users')
def get_users():
    statement = select(models.User)
    results = session.exec(statement).all()
    return results


@app.post('/users', response_model=models.User, status_code=status.HTTP_201_CREATED)
def create_user(user: models.UserBase):
    db_user = models.User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return user
"""

def error_message(message):
    print(message)
    return {
        'error': message
    }

def create_token(user_id: int):
    token = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(24)))
    expiration_date = int(time.time()) + 1000
    user_token_model = models.UserToken(token=token,user_id=user_id,expires=expiration_date)
    session.add(user_token_model)
    session.commit()
    return token



@app.post('/info', response_model=models.ApiUser, status_code=status.HTTP_201_CREATED)
def save_api_user(api_user: models.ApiUser):
    statement = select(models.ApiUser).where(models.ApiUser.api_user_id == api_user.api_user_id)
    result = session.exec(statement).first()
    if result is None:
        session.add(api_user)
        session.commit()
        session.refresh(api_user)
        return api_user
    raise HTTPException(400, detail= error_message('This api_id info already exists'))

@app.get('/info_api_users')
def get_all_api_users_info():
    statement = select(models.ApiUser)
    results = session.exec(statement).all()
    return results


@app.get('/')
async def home():
    return 'auth_ms'

@app.get('/token_google_auth')
async def token_after_google_auth(sub: str,email: str, provider: str):
    
    statement = select(models.ApiUser).where(models.ApiUser.api_user_id == sub)
    result = session.exec(statement).first()
    if result:
        print('This oauth user already exists in our db')
        return create_token(result.user_id)
    print('Creating new oauth user')
    new_user = models.ApiUser(api_user_id=sub,email=email,provider=provider)
    session.add(new_user)
    session.commit()
    statement = select(models.ApiUser).where(models.ApiUser.api_user_id == sub)
    result = session.exec(statement).first()
    return create_token(result.user_id)

@app.get('/info_tokens')
def get_all_users_tokens():
    statement = select(models.UserToken)
    results = session.exec(statement).all()
    return results

@app.get("/userid_from_token")
def userid_from_token(token: str):
    #print(f'user_token w auth1: {token}')
    statement = select(models.UserToken).where(models.UserToken.token == token)
    result = session.exec(statement).first()
    #print(f'result w auth1: {result}')
    if result:
        return result.user_id
    return 0
"""