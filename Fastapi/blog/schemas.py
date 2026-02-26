from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import List, Optional


# ---------- Blog Create ----------
class BlogCreate(BaseModel):
    title: str
    body: str


class BlogUpdate(BaseModel):
    title: str
    body: str 
    model_config = ConfigDict(from_attributes=True)


# ---------- User Response ----------
class ShowUser(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)


# ---------- Blog Response ----------
class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    creator: ShowUser

    model_config = ConfigDict(from_attributes=True)


# ---------- User Create ----------
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=50)


# ---------- User Response With Blogs ----------
class ShowUserWithBlogs(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[ShowBlog] = []

    model_config = ConfigDict(from_attributes=True)


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None