from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from src.models import Gender, Role, User, UpdateUser

app = FastAPI()

db: List[User] = [
  User(
    id= uuid4(),
    first_name='John',
    last_name="Markson",
    gender=Gender.male,
    roles=[Role.user],
  ),
  User(
    id= uuid4(),
    first_name='Jane',
    last_name="Markson",
    gender=Gender.female,
    roles=[Role.admin],
  ),
  User(
    id= uuid4(),
    first_name='Arvind',
    last_name="T",
    gender=Gender.male,
    roles=[Role.user],
  ),
  User(
    id= uuid4(),
    first_name='Megha',
    last_name="Kulkarni",
    gender=Gender.male,
    roles=[Role.user, Role.admin],
  ),
]

@app.get("/api/v1/users")
async def get_users():
  return db

@app.get("/")
async def greet_hello():
  return "Hello World !!!!"

@app.post("/api/v1/users")
async def create_user(user: User):
  db.append(user)
  return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(id:UUID):
  for user in db:
    if user.id == id:
      db.remove(user)
      return
  raise HTTPException(
    status_code=404, detail=f"Delete user with id={id} failed, id could not be found!!!"
  )

@app.put("/api/v1/users/{id}")
async def update_user(id:UUID, user_update: UpdateUser):
  for user in db:
    if user.id == id:
      if user_update.first_name is not None:
        user.first_name = user_update.first_name
      if user_update.last_name is not None:
        user.last_name = user_update.last_name
      if user_update.roles is not None:
        user.roles = user_update.roles
      return user.id
  HTTPException(status_code=404, detail=f"Update user with id={id} failed, id could not be found!!!")

@app.get("/nam_chubbi")
async def my_call():
  return {"Ilove you" : "nam chubbi !!!!"}