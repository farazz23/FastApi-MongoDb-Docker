def individual_todo(todo) -> dict :
  return {
    "id": str(todo["_id"]),
    "title" : todo["title"],
    "description" : todo["description"],
    "status":todo["is_completed"]
  }
  
def all_list(todos) -> list :
  return [individual_todo(todo) for todo in todos]