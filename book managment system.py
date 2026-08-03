class Book:
    def __init__(self, book_id, name, author, price, quantity):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.price = price
        self.quantity = quantity
    def discount(self):
        if self.price >= 1000:
            return self.price - (self.price * 0.20)
        elif self.price >= 500:
            return self.price - (self.price * 0.10)
        else:
            return self.price
    def stock(self):
        if self.quantity > 0:
            return "Stock is Available"
        else:
            return "Out of Stock"
    def display(self):
        print("Book ID :", self.book_id)
        print("Book Name :", self.name)
        print("Author :", self.author)
        print("Price :", self.price)
        print("Quantity :", self.quantity)
        print("Discount Price :", self.discount())
        print("Stock Status :", self.stock())
        print("-----------------------------")

B1 = Book(2411, "Wings of Fire", "A.P.J. Abdul Kalam", 700, 5)
B2 = Book(2412, "Rich Dad Poor Dad", "Robert Kiyosaki", 1200, 0)
B1.display()
B2.display()