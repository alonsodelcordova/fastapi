from app.models.authModel import User, Token
import uuid

def getUser(username:str)->User:
    user = User.get_or_none(User.username == username)
    return user

def generateToken(user:User)-> Token:
    token_md = Token.get_or_none(Token.user == user)
    if token_md is None:
        token_md = Token.create(user=user, token=str(uuid.uuid4())+"."+str(user.id))
    return token_md