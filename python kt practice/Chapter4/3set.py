# set {}
my_set = {1,2,3,4,5,5,5,55,5}
print(type(my_set))

# add() method adds an element to the set
my_set.add(6)
print(my_set)
my_set.add(5)
print(my_set)
# copy() method creates a shallow copy of the set
new_set = my_set.copy()
# clear() method removes all the elements from the set
my_set.clear()
print(my_set)
print(type(my_set))

shop = {'milk', 'bread', 'eggs', 'cheese', 'butter'}
print(shop)
shop.add('yogurt')
shop.add('cereal')
print(shop)

shop2 = {'pencil', 'notebook', 'eraser', 'sharpener','milk','bread'}

# difference() method returns the difference of two or more sets as a new set
print(shop2.difference(shop))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set2.difference(set1))

# discard() method removes the specified item from the set
set1.discard(3)
print(set1)
# remove
set1.remove(5)
print(set1)
# pop
print(set1.pop())
print(set1)
# pop method in shop2
print(shop2)
print(shop2.pop())
print(shop2)

# difference update
s1 = {1,2,3,4}
s2 = {3,4,5,6}
s1.difference_update(s2)
print(s1)

s3={4,6,8,10}
s4={11,8,6,25}
# intersection printing the same element in both set
int_set = s3.intersection(s4)
print(int_set)

# symmetric difference
set1 = {1,2,3,4}
set2 = {3,4,5,6}
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)

# union
uni_set = set1.union(set2)
print(uni_set)

# update
set2.update(set1)
print(set2)
print(set1)

# len
print(len(set1))

# in operator
print(shop2)
print('pencil' in shop2)
print(372 in set2)