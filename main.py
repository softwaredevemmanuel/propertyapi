from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import App.database as database
from App import routers

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Allow requests from localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["POST", "PATCH", "DELETE"]
    )

app.include_router(routers.router)


@app.get('/')
async def hello():
    return {"greeting":"Property"}

