from app.schemas import authSchema
from app.services import authService
from fastapi import HTTPException

def loginController(data:authSchema.LoginRequestModel)-> authSchema.LoginResponseModel:
    resp_service = authService.getUser(data.username)
    if resp_service is None:
        raise HTTPException(status_code=404,detail="User not found")
    if resp_service.password != data.password:
      raise HTTPException(status_code=400, detail="Password Incorrect")
    token = authService.generateToken(resp_service)
    return token

def registerController(data:authSchema.RegisterRequestModel) -> authSchema.RegisterResponseModel:
  
  resp_service = authService.registerUser(data.dict())
  return resp_service