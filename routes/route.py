from fastapi import APIRouter, HTTPException
from database import db_config, models, schema
from bson import ObjectId
from datetime import datetime 


router = APIRouter(tags=['Todo'], prefix='/todo')
collection  = db_config.collection
all_list = schema.all_list
TODO = models.Todo


@router.post("/")
async def create_post(new_todo : TODO):
  try:
    response = collection.insert_one(new_todo.dict())
    return {
      "status": 200,
      "data" : {
        "id": str(response.inserted_id)
      }
    }
  except Exception as e:
    raise HTTPException(status_code=500 ,
                         detail=f"Something Went Wrong {e}")

@router.get("/")
async def get_all_todos():
  data = collection.find();
  return all_list(data)


@router.put("/{id}")
async def update_todo(id , updated_todo:TODO):
  try:
    is_todo_exist = collection.find_one({"_id":ObjectId(id) , "is_deleted":False })
    if not is_todo_exist:
      raise HTTPException(status_code=404, 
                          detail=f"User with id: {id} Not Found")
    updated_todo.updated_at = int(datetime.now().timestamp())
    resp = collection.update_one({"_id": id}, {"$set" : updated_todo.dict()})
    return {
      "status" : 200,
      "data" : {
        "message" : "Todo Updated"
      
      }
    }
  except Exception as e :
    raise HTTPException(status_code=500 ,
                        detail=f"Something Went Wrong {e}")
    
# @router.get("/{id}")
# async def get_todo(id : str):
#   try:
    
#     todo = collection.find_one({"_id" : ObjectId(id)})
#     if not todo:
#       raise HTTPException(status_code=404, 
#                           detail=f"user not Found ")
#     return todo   
#   except Exception as e:
#     raise HTTPException(status_code=500 ,
#                         detail=f"Something Went Wrong {e}") 
    