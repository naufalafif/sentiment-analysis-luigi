from fastapi import FastAPI, Request
from app.src.api import api

def create_application(name, config):
    datetime_version = config.get('datetime')
    application = FastAPI(title=name)
    application.include_router(api.router, prefix='/v1')
    application.state.version = datetime_version

    return application

app = create_application("Sentiment Analisys + Luigi", {'datetime': '2020-12-11'})

@app.get('/')
def index(request: Request):
    return {
        "v1": f"{request.url}v1"
    }
