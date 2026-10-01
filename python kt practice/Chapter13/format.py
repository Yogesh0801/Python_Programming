# a = 43
# b = 12
# print(a+b)
# print(f"The sum of {a} and {b} is {a+b}")

# a = "{0} {1}".format("a", "b")
# print(a)


# classperson = "{2} and {0} and {1}".format("subha","annapurna","mythili")
# print(classperson)



classperson=lambda name,age,gender : "{0} is {1} years old and {2}".format(name,age,gender)
print(classperson("John",20,"male"))
