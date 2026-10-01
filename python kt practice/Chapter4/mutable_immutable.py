# mutable = Changable (we can change the value)
# mutable = (list, set, dict) 3

# immutable = Unchangable (we cannot change the value)
# immutable = (int, float,complex, bool, str, tuple) 6
a = 10
print("Before changing the value of a:", a)
#a[0]= 2
#print("After changing the value of a:", a)
b = 67.89
print("Before changing the value of b:", b)
# b [1] = 5
# print("After changing the value of b:", b)
# bool
c = True
print("Before changing the value of c:", c)
print(id(c))
# c[1]= False
# print(c)
# print(id(c))
# print("After changing the value of c:", c)

# str
d = "Hello"
print(d)
# d[0] = "h"
# print(d)

# tuple
e = (1, 2, 3)
print(e)
# e[0] = 4
# print(e)

# mutable = (list, set, dict)
# list
f = [1,3,5,'yogesh',79.7]
print("before changing the value of f:", f)
f[0] = 2
f[3] = 7
f[4] = 9
print("after changing the value of f:", f)

# set
g = {1, 2, 3, 4, 5}
print("before changing",g)
g.add(6)
print("after changing",g)
g.remove(2)
print("after removing 2",g)
#dict
h = {1: "yogesh", 2: "kumar", 3: "singh"}
print("before changing",h) 
h[1] = "yashu"
print("after changing",h)
print(h.keys())
print(h.values())