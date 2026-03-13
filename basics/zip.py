#zip is used when you have to iterate multiple values in parallel
ids = ["DS001","DS002","DS003","DS004"]
names = ["Aarush", "Anay" ,"Abhiraj", "Harry"]
interests = {"Programming", "Chess" ,"Physics" ,"Programming"}
for id, name, interest in zip(ids, names, interests):
    print(f"ID : {id}, NAME : {name} and interested in {interest}")