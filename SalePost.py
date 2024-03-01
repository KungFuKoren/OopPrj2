from Post import Post


class SalePost(Post):
    def __init__(self, user, type, product, price, location):
        super().__init__(user, type, product)
        self.price = price
        self.location = location
        self.available = True

    def __str__(self):
        new_line = '\n'
        if self.available:
            return f"{self.user.userName} posted a product for sale:{new_line}For sale! {self.content}, price: {self.price}, pickup from: {self.location}"
        return f"{self.user.userName} posted a product for sale:{new_line}Sold! {self.content}, price: {self.price}, pickup from: {self.location}"

    def discount(self, discount, password):
        if self.user.passWord != password:
            raise Exception("Wrong password")
        self.price = self.price * (1 - (discount / 100))
        print(
            f"Discount on {self.user.userName} product! the new price is: {self.price}")

    def sold(self, password):
        if isinstance(password, str):
            if self.getUser().passWord == password and self.available == True:
                self.available = False
                print(f"{self.getUser().getName()}'s product is sold")
            else:
                if self.getUser().passWord != password:
                    raise Exception("Invalid password")
                else:
                    raise Exception("Item already sold")
        else:
            raise Exception("invalid input")
