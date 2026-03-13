# enumarete funtion lets you keep a record of the index of the current iterating obj when using for loop

names = ["Aarush", "Anay", "Abhiraj", "Harry", "David"]

for name in names:
    print(name, end=" ")
# OUTPUT : Aarush Anay Abhiraj Harry David
print("\n")

# what if you need to keep the record of the index?

for index, name in enumerate(names):
    print(f"INDEX : {index}, NAME : {name}")
# OUTPUT :
# INDEX : 0, NAME : Aarush
# INDEX : 1, NAME : Anay
# INDEX : 2, NAME : Abhiraj
# INDEX : 3, NAME : Harry
# INDEX : 4, NAME : David
print("\n")
# OPTIONALLY you can add another argument to specifiy the starting.
for index, name in enumerate(names, 1):
    print(f"SNO : {index}, NAME : {name}")
# OUTPUT :
# SNO : 1, NAME : Aarush
# SNO : 2, NAME : Anay
# SNO : 3, NAME : Abhiraj
# SNO : 4, NAME : Harry
# SNO : 5, NAME : David
