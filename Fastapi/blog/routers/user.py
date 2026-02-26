from typing import List
from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from ..import schemas ,database,models,oauth2
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
                   )
get_db = database.get_db

# Create User
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
  return user.create(request, db)


# # Get Single User
# @router.get("/{id}",response_model=schemas.ShowUser)
# def get_user(id: int, db: Session = Depends(get_db)):
#     return user.show(id,db)
@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(
    id: int,  # ✅ id yaha receive karna jaruri hai
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    return user.show(id, db)
