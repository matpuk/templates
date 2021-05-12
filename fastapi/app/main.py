from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .controllers import health
from .controllers import workspace

api_prefix = '/rest-svc/api/v1'

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    # allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(health.router, prefix=api_prefix)
app.include_router(workspace.router, prefix=api_prefix)
