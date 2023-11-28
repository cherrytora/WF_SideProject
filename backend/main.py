from typing import Optional
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from common.wf_db_connector import register

app = FastAPI()


class Authz(BaseModel):
    employee: str
    name: str
    department: str
    acct: str
    pwd: str
    auth: str


@app.post("/insert_authz")
async def insert_authz(insert_authz: Authz):
    employee = insert_authz.employee
    name = insert_authz.name
    department = insert_authz.department
    acct = insert_authz.acct
    pwd = insert_authz.pwd
    auth = insert_authz.auth
    insert_data = (employee, name, department, acct, pwd, auth)
    register(insert_data)
    return {
        "message": 'Success',
        "insert_data": insert_data
    }


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8787, reload=True)
