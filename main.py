

#The dictionary is in the form of Book_Database=[Book_ID]:{Genre,Title ,Author}

Book_Database ={}

Book_Database['001']={'Genre': 'Action and Adventure',
                      'Title': 'The Three Musketeers',
                      'Author1': 'Alexander Dumas'}

Book_Database['002']={'Genre': 'Graphic and Comic',
                      'Title': 'Treasure Island',
                      'Author': 'Robert Louis Stevenson'}

Book_Database['003']={'Genre': 'Action and Adventure',
                      'Title': 'Life of Pi',
                      'Author': 'Yann  Martel'}

Book_Database['004']={'Genre': 'Graphic and Comicr' ,
                      'Title': 'Black Panther',
                      'Author': 'Ta-Nehisi Coates and Brian Stelfreeze'}

Book_Database['005']={'Genre': 'Graphic and Comic',
                      'Title': 'Batman;The Dark Knight Returns',
                      'Author': 'Frank Miller, Klaus Janson and Lynn Varley'}

Book_Database['006']={'Genre': 'Horror',
                      'Title': 'Bird Box',
                      'Author': 'Josh Malerman'}

Book_Database['007']={'Genre': 'Horror',
                      'Title': 'Carrie',
                      'Author': 'Stephen King'}

Book_Database['008']={'Genre': 'Horror',
                      'Title': 'The Haunting of Hill House',
                      'Author': 'Shirley Jackson'}

Book_Database['009']={'Genre': 'Romance',
                      'Title': 'Brazen and The Beast ',
                      'Author': 'Sarah MacLean'}

Book_Database['0010']={'Genre': 'Romance',
                       'Title': 'Wife by Wednesday',
                       'Author': 'Catherine Bybee'}

Book_Database['0011']={'Genre': 'Romance',
                       'Title': 'Virgin River',
                       'Author': 'Robyn Carr'}

Book_Database['0012']={'Genre': 'Romance',
                       'Title': 'In Bed with the Devil',
                       'Author': 'Lorraine Heath'}

Book_Database['0013']={'Genre': 'Action and Adventure',
                       'Title': 'Mockingjay',
                       'Author': 'Suzanne Collins'}

Book_Database['0014']={'Genre': 'Action and Adventure',
                       'Title': 'The Odessey',
                       'Author': 'Hommer'}

Book_Database['0015']={'Genre': 'Action and Adventure',
                       'Title': 'Moby-Dick',
                       'Author': 'Herman Melville'}

Book_Database['0016']={'Genre': 'Romance',
                       'Title': 'Mine Till Midnight',
                       'Author': 'Lisa Kleypas'}

Book_Database['0017']={'Genre': 'Graphic and Comic',
                       'Title': 'Elf-quest',
                       'Author': 'RWendy Pini and Richard Pini'}

Book_Database['0018']={'Genre': 'Action and Adventure',
                       'Title': 'The Adventures of Huckleberry Finn',
                       'Author': 'Mark Twain'}

Book_Database['0019']={'Genre': 'Detective and Mystery',
                       'Title': 'The Adventures of Sherlock Holmes',
                       'Author': 'Sir Arthur Conan Doyle'}

Book_Database['0020']={'Genre': 'Fantacy',
                       'Title': 'Circe',
                       'Author': 'Madeline Miller'}


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
