class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addbook(self , book):
        self.books.append(book)
        self.nobooks = len(self.books) 



    def showInfo(self):
        print(f"The library has {self.nobooks} books. the books are")
        for book in self.books:
            print(book)
   
l1 = library()
l1.addbook("harry potter")
l1.addbook("harry potter1")
l1.addbook("harry potter2")
l1.showInfo()
 