class Phone:

    def __init__(self, brandname, modelname, price):
        self.brandname = brandname
        self.modelname = modelname
        self.price = price

    def Introduction(self):
        print(f"This iphone is made by {self.brandname} and its model is {self.modelname}. It cost {self.price}")


class Smartphone(Phone):
    def __init__(self, brandname, modelname, price, displaysize, internalmemory, batterylife):
        super().__init__(brandname, modelname, price)
        self.displaysize = displaysize
        self.internalmemory = internalmemory
        self.batterylife = batterylife

class IPhone(Smartphone):
    def __init__(self, brandname, modelname, price, displaysize, internalmemory, batterylife, camera, storage, plugins):
        super().__init__(brandname, modelname, price, displaysize, internalmemory, batterylife)
        self.camera = camera
        self.storage = storage
        self.plugins = plugins
obj1 = IPhone("Apple", "Orage", "200", "2m, 8c","90g","3 hours", "HD Life", "200g", "Multiple")
obj1.Introduction()