from Mukund import Mukund

storage = Mukund('MukundX') # You can use it even passing the name parameter it will create a folder name Storage

collection = storage.database('users') #This makes a file called users.json in the Storage folder or whatever u named that folder

print("Put")
collection.put(
    "6867879163",
    {"name": "Random", "username": "@random"}
)
print("\n\n")

print("Get")
print(collection.get("6867879163"))

random = collection.get("6867879163")
print(random)

print("\n\n")

print("Increment & Decrement")
collection.put(
    "6867879165",
    {"name": "Robo", "age": 16, "class": 11}
)
collection.increment("6867879165")
print(collection.get("6867879165"))
collection.decrement("6867879165")
print(collection.get("6867879165"))
print("\n\n")

print('All Function')
print(collection.all())
print("\n\n")

print("Fetch")
print(collection.fetch()) # If no query is passed works like all function but don't provide which key value that data belongs too as all fucntion does
print(collection.fetch(query_params={"name?contains": "Robo"}))
print("\n\n")

print("Query")
print(collection.wquery("Random"))
print(collection.query(condition_func=lambda collection: collection.get("age", 0) > 15, limit=5))
print("\n\n")

print("Update")
collection.update("6867879163", updated_values={"name": "RandomGirl"})
print(collection.get("6867879163"))
print("\n\n")

print("Count")
print(collection.count())
print("\n\n")

print("Flush")
collection.flush() # Warning this deletes all the data in the collection
