class Vertex():
    def __init__(self, location):
        self.location = location


class Warehouse(Vertex):
    def __init__(self, location, products):
        Vertex.__init__(self, location)
        self.products = products


class Costumer(Vertex):
    def __init__(self, location, products):
        Vertex.__init__(self, location)
        self.products_indexes = products
