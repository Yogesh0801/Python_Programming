# Mutable data Type
my_dict = {'name':'yogesh', 'age': 25, 'city': 'New York'}
print(my_dict)
# clear() method removes all the elements from the dictionary
# my_dict.clear()
print("After clearing the dictionary:", my_dict)
print(type(my_dict))

# copy() method creates a shallow copy of the dictionary
new_dict = my_dict.copy()
print(new_dict)

# get() method returns the value of the specified key
print(new_dict.get('name'))
print(new_dict.get('age'))

# items() total number of items in the dictionary
print(new_dict.items())

# keys() total keys in the dictionary
print(new_dict.keys())

# values() total values in the dictionary
print(new_dict.values())

# pop() specifies key and remove the item
print(new_dict.pop('age'))
print(new_dict)

# popitem() removes the last item
print(new_dict.popitem())
print(new_dict)

# len() method returns the number of items in the dictionary
print(len(new_dict))
print(len(my_dict))

# update() method updates the dictionary with the specified key-value pairs
new_dict.update({'country': 'USA', 'age': 30,'position': 'Developer'})
print(new_dict)
print(len(new_dict))

# del() method removes the specified item from the dictionary
del new_dict['position']
print(new_dict)
new_dict.pop('age')
print(new_dict)

# in operator checks if the specified key is present in the dictionary
print('age' in new_dict)

del new_dict
# print(new_dict)  # This will raise an error since new_dict is deleted