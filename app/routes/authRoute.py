from fastapi import APIRouter
from app.schemas import authSchema
from app.controllers import authController

router = APIRouter(
    prefix="/api/auth",
    tags=['Authenticate'],
    responses={ 404: {'description':'Not Found'}}
)

@router.post('/login', 
    description='Inicio de Sesion',
    response_model=authSchema.LoginResponseModel
)
def login(data:authSchema.LoginRequestModel):
    newData = authController.loginController(data)
    return newData

@router.post(
    '/register',
    description='Register User',
    response_model=authSchema.RegisterResponseModel
)
def register(data:authSchema.RegisterRequestModel):
    newUser = authController.registerController(data)
    return newUser