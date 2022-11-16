from app.models.authModel import User, Token
import uuid
from fastapi import HTTPException
def getUser(username:str)->User:
    user = User.get_or_none(User.username == username)
    return user

def generateToken(user:User)-> Token:
    token_md = Token.get_or_none(Token.user == user)
    if token_md is None:
        token_md = Token.create(user=user, token=str(uuid.uuid4())+"."+str(user.id))
    return token_md

def registerUser(data:dict) -> User:
    user_md = User.get_or_none(User.username == data['username'])
    if user_md is None:
        try:
            new_user = User.create(**data) 
            return new_user
        except Exception:
            raise HTTPException(status_code=400, detail="Ocurrió un error")
       
    else:
        raise HTTPException(status_code=400, detail="Usuario ya registrado")
    