from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("user/{username}/{age}")
async def registered_user(username: str, age: int) -> str:
    current_id = str(int(max(users, key=int)) + 1)
    users[current_id] = f"Имя: {username}, возраст: {age}"
    return f"User {current_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: Annotated[int, Path(gt=0)]) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    users.pop(user_id)
    return f"The user {user_id} is deleted"

