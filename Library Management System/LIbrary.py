# MINI PROJECT FOR LIBRARY
# Method to display all books
# Method to Lend Book
# Method to display who owns the book if not present
# Method to add books/donate
# Method to return book
# Create a library which takes a constructor list of all books in the library and library name
# Create dictionary who owns which book

dict_log = {}

class Library:
    def __init__(self,list_of_books,library_name):
        self.list_of_books=list_of_books
        self.library_name=library_name

    def display(self):
        return f"In {self.library_name} library books present are {self.list_of_books}"

    def lend(self):
        lender_name=input("Hello Dear Reader,Tell Us your Name :")
        lend_book=input("Tell us which book you would love to read :")
        if lend_book in self.list_of_books:
            print("The book is available,You can Read It;")
            self.list_of_books.remove(f"{lend_book}")
            dict_log[f"{lend_book}"]=f"{lender_name}"
            print(dict_log)
        else:
            a=str(f"{lend_book}")
            print(a)
            print(f"The book is not currently available,it is with {dict_log[a]}")



    def return_book(self):
        return_name=input("Hello Dear Reader,Tell Us your Name :")
        return_book=input("Tell us which book you are returning :")
        del dict_log[f"{return_book}"]

    def donate_book(self):
        donateed_book=input("Which book you are donating :")
        self.list_of_books.append(f"{donateed_book}")


harrylibrary=Library(["Harry Potter","The Lord of the Rings","The Book Thief"],"Harry Readers")

while True:
    ask=int(input("Tell us Reader how can i help you :\n (press 1 : To display list of all books). \n (press 2: To lend) \n (press 3 : to return) \n (press 4 : To donate book ) :"))
    if ask==1:
        print(harrylibrary.display())
    elif ask==2:
        harrylibrary.lend()
    elif ask==3:
        harrylibrary.return_book()
    else:
        harrylibrary.donate_book()
