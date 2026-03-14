# Python Dictionaries – Key-Value Storage

# Create a dictionary using curly braces
pizza = {
    'name': 'Margherita Pizza',       # key: 'name', value: 'Margherita Pizza'
    'price': 8.9,                     # key: 'price', value: 8.9
    'calories_per_slice': 250,        # key: 'calories_per_slice', value: 250
    'toppings': ['mozzarella', 'basil']  # key: 'toppings', value: list of toppings
}

# Alternative: Create dictionary with dict() constructor
pizza_alt = dict([
    ('name', 'Margherita Pizza'),
    ('price', 8.9),
    ('calories_per_slice', 250),
    ('toppings', ['mozzarella', 'basil'])
])

# Access a value using its key
print(pizza['name'])  # Output: 'Margherita Pizza'

# Update a value or add new key-value pair
pizza['name'] = 'Margherita'
pizza['total_time'] = 25

# Access values safely with .get() to avoid KeyError
toppings = pizza.get('toppings', [])  # Returns [] if 'toppings' key missing

# Get all keys, values, or items
keys = pizza.keys()     # dict_keys(['name', 'price', 'calories_per_slice', 'toppings', 'total_time'])
values = pizza.values() # dict_values([...])
items = pizza.items()   # dict_items([('name', ...), ...])

# Remove items
removed_value = pizza.pop('price', 0)   # Removes 'price', returns its value, default 0 if missing
last_item = pizza.popitem()             # Removes last inserted item

# Clear all items
# pizza.clear()

# Merge/update dictionary with another
pizza.update({'price': 15, 'total_time': 25})  # Overwrites 'price', adds 'total_time'

# Final dictionary state
print(pizza)

# Sample dictionary
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

# 1. Loop over values
for price in products.values():
    print(price)  # 990, 600, 250, 70

# 2. Loop over keys
for product in products.keys():
    print(product)  # 'Laptop', 'Smartphone', 'Tablet', 'Headphones'

# 3. Loop over keys directly (shorthand)
for product in products:
    print(product)

# 4. Loop over key-value pairs as tuples
for pair in products.items():
    print(pair)  # ('Laptop', 990), ...

# 5. Loop over key-value pairs with separate variables
for product, price in products.items():
    print(product, price)  # 'Laptop' 990, ...

# 6. Apply 20% discount to all products
for product, price in products.items():
    products[product] = round(price * 0.8)
print(products)  
# {'Laptop': 792, 'Smartphone': 480, 'Tablet': 200, 'Headphones': 56}

# 7. Loop with index using enumerate() – over keys
for index, product in enumerate(products):
    print(index, product)  # 0 'Laptop', 1 'Smartphone', ...

# 8. Loop with index – over values
for index, price in enumerate(products.values()):
    print(index, price)  # 0 792, 1 480, ...

# 9. Loop with index – over items
for index, pair in enumerate(products.items()):
    print(index, pair)  # 0 ('Laptop', 792), 1 ('Smartphone', 480), ...

# 10. Loop with custom starting index
for index, pair in enumerate(products.items(), 1):
    print(index, pair)  # 1 ('Laptop', 792), ...