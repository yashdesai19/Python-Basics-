from fastapi import FastAPI
from .database import engine
from . import models
from blog.routers import blog, user,authentication

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
