# local variable: if we are created the variable inside the function so we 
# can use it inside only we cant use outside
# global variable :
# we can use inside or outside also
# a = 89
a = 78
def fun():
    #
    global a
    a = 65
    print(a)
fun()
print(a)