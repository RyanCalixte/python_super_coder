# functions with all types of parameters

# PADK
# Normal Parameters
# Arguments
# Default Parameters
# Keyword Arguments

def func(name, *args, lastname = "calixte", **kwargs):
    print(name)
    print(args)
    print(lastname)
    print(kwargs)


func("ryan", 1,2,3,4, "wankhede", x=1, y=2, z=3)

