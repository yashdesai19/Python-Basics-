from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

# ================== GET ALL BLOGS ==================
@router.get("/", response_model=List[schemas.ShowBlog])
def all(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    return blog.get_all(db)


# ================== CREATE BLOG ==================
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create(
    request: schemas.BlogCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    return blog.create(request, db, current_user)


# ================== GET SINGLE BLOG ==================
@router.get("/{id}", response_model=schemas.ShowBlog)
def show(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    return blog.show(id, db)


# ================== UPDATE BLOG ==================
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id: int,
    request: schemas.BlogCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    return blog.update(id, request, db)


# ================== DELETE BLOG ==================
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    return blog.destroy(id, db)