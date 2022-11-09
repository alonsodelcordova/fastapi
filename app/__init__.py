from fastapi import FastAPI
from . import db
from app.models import authModel
from app.routes import authRoute
## defined APP MAIN
app = FastAPI(
    title="API de Blog",
    description="Blog universal",
    version="0.0.1"
)

def startApp() -> FastAPI:
    app.include_router(authRoute.router)
    return app
    #eventos del server

# evento del servidor
@app.on_event("startup")
async def startup():
    db.conect_db()
    """create tables"""
    db.database.create_tables(
        [authModel.User, authModel.Token], 
        safe=True
    )

    
@app.on_event("shutdown")
async def shutdown():
    db.disconnect_db()

