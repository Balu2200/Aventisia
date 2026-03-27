from fastapi import FastAPI
from routes import github


app = FastAPI(title="GitHub Connector")

app.include_router(github.router, prefix="/github", tags=["GitHub"])
