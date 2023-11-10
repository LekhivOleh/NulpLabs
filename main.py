class Library:
    def __init__(self):
        self.reserved_books = ["aaaa", "asas", "ssss"]
        self.books_map = {1: "book_1", 2: "book_2", 3: "book_3", 4: "book_4", 5: "book_5", 6: "book_6", 7: "book_7", 8: "book_8", 9: "book_9"}

    def reserve_book(self, book_id):
        if book_id not in self.reserved_books and book_id in self.books_map.keys():
            self.reserved_books.append(book_id)
            print(f"Book {book_id} successfully reserved")
        else:
            print("Exception")

class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title

library = Library()

library.reserve_book("dsds")
library.reserve_book("penususasvs")

#_____________________________________________

marks1 = [1,2,3,4,5,6,7,8,9]
marks2 = [10,20,30,40,50,60,70,80,96]
def avarage_mark(*args):
    res = sum(*args)/len(*args)
    print(f"avarage mark is {res}")

avarage_mark(marks1)
avarage_mark(marks2)
