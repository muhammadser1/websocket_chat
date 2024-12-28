from fastapi import FastAPI
from routes.home import router as home_router
from routes.websocket import router as websocket_router

app = FastAPI()

app.include_router(home_router)
app.include_router(websocket_router)
