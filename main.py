from database import *


def view_all_books():
    print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in Book_Database.items()) + "}" + "\n")



def change_detail():
    Book_ID = input("Input the Id of The book you want to modify: ")
    if Book_ID in Book_Database:
        Title = str(input("Input a new Title for the book: "))
        Genre=str(input("Input a new genre for the book: "))
        Author =str(input("Input a new author for the book: "))
        Book_Database.update({Book_ID: {
            "Genre": Genre,
            "Title": Title,
            "Author" : Author
            }})
        print("The details of the book has been changed successfully")
    else:
        print("Book does not exist in database")


def add_book():
    Book_ID = (input("Input the Id of the new book you want to add: "))
    Title = str(input("Input it's Title: "))
    Genre = str(input("Input it's genre: "))
    Author =str(input("Input it's author: "))
    Book_Database.update({Book_ID: {
            "Genre": Genre,
            "Title": Title,
            "Author" : Author
            }})


def main():
    print(
        "1: View all books in database \n2: Modify the detail of an existing book \n3: Add a new book to the database \n4: Exit the program")
    opt = int(input("Choose your option: "))
    while opt != 4:
        if opt == 1:
            print("Below are the books present in your database")
            view_all_books()
            return main()
        elif opt == 2:
            change_detail()
            return main()
        elif opt == 3:
            add_book()
            print("Book has been added successfully")
            return main()
        elif opt == 4:
            break
        else:
            print("Invalid Input \nEnter 1-4")
            return main()


main()
