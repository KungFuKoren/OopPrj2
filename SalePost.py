from Post import Post

class SalePost(Post):
    def __init__(self, user, type, product, price, location):
        super().__init__(user, type, product)
        self.price = price
        self.location = location
    
    def print(self):
        print("product = ", self.content)
        print("price = ",self.price)
        print("location = ",self.location)
