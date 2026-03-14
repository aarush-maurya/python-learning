# a set is a collection of non repeating well defined objects
natural_set = {1, 2, 3, 4, 5, 6}
whole_set = {0, 1, 2, 3, 4, 5, 6, 7}

# isubset()

print(natural_set.issubset(whole_set))  # True
print(whole_set.issubset(natural_set))  # False
print()
# issuperset()

print(natural_set.issuperset(whole_set))  # False
print(whole_set.issuperset(natural_set))  # True

# Operations

# Union(|) [returns a set which has all the elements in both the set]

a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9, 10}

one_to_ten = a | b
print()
print(one_to_ten)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# intersection(&) [returns a set which has only the common elements in the two sets]

c = a & b
print()
print(c)  # 5

# diffrence (-) [if a - b, then returns a set which has all the elements in set a except the common elements]
d = a - b
print()
print(d)  # {1, 2, 3, 4}

# symmetric diffrence (^) [if a ^ b, then returns a set which is in either a or b but not the ones which is common in both sets]
e = a ^ b
print()
print(e)  # {1, 2, 3, 4, 6, 7, 8, 9, 10}

# you can also add elements to a set by my_set.add(element)

# my_set.isdisjoint(your_set) returns a bool value

# my_set.remove(element) remove an element and if the element isnt there then it raises KeyError but my_set.discard(element) does not
