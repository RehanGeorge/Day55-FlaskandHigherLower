# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}({args[0]}, {args[1]}, {args[2]})")
        result = function(args[0],args[1],args[2])
        print(f"It returned {result}")
    return wrapper

@logging_decorator
def multiply(a,b,c):
    return a*b*c


# Use the decorator 👇

multiply(1,2,3)