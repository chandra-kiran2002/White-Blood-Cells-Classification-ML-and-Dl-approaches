
a=10
def make_h1(function):
    def inner(x):
        print("<h1>"+function(x)+" "+str(x)+"</h1>")
    return inner

@make_h1
def make(a):
    return "hi"

make(a)