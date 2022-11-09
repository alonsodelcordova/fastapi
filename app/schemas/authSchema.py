
from typing import Optional
from pydantic import BaseModel
from app.utils import peeweeUtil

class LoginRequestModel(BaseModel):
   username: str
   password: str

class UserRequestModel(LoginRequestModel):
   email: Optional[str] = None
   first_name: Optional[str] = None
   last_name: Optional[str] = None
   phone: Optional[str] = None
   address: Optional[str] = None
   city: Optional[str] = None
   is_active: Optional[bool] = False
   class Config:
      orm_mode = True
      getter_dict = peeweeUtil.PeeweeGetterDict

class LoginResponseModel(BaseModel):
   token: str
   user: UserRequestModel
   class Config:
      orm_mode = True
      getter_dict = peeweeUtil.PeeweeGetterDict