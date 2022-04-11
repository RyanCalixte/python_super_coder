# kwargs -> keyword arguments

def func(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")


func(a=1, b=2, c="name")


data = dict(
    name = "ryan",
    age = 12,
    job = "python developer",
)

func(**data)
