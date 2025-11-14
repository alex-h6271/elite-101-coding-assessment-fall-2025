from library_books import library_books

from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

# The purpose of this function is as the name
# suggests, to lopp through the dictionary library_books
# and to print out its contents.

def display_books():
    for book in library_books:
        print("----------------------------")
        for key, value in book.items():
             print(f"{key}:{value}") 
    print("___________________________")

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

# The purpose of this function is as the name
# suggests, to allow the user to search the library_books
# dictionary and print out the matching results.

def search_books():
    search = str(input('Please input the search term (Author or Genre): ')).title()
    for book in library_books:
        if book['author'] == search or book['genre'] == search:
            print("----------------------------")
            for key, value in book.items():
                print(f"{key}:{value}") 
            print("___________________________")
         
# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

# I honestly tried to get the daterime module working,
# but was ultimately unable to figure out how to implement it properly.

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

# I implemented two functions that allow the user to navigate
# the program through a menu system.

def display_menu():
    print('\n**Very Real Library Inventory System**')
    print("------------------------------------------")
    print(f'What would you like to do?')
    print('1. View Store Inventory')
    print('2. Search Store Inventory')
    print('3. Checkout a Book')
    print('4. Return a Book')
    print('5. View Overdue Books')
    print('6. Exit')

def user_selection():
    
    user = int(input('Please choose a service: '))

    if user == 1:
        display_books()
    elif user == 2:
        search_books()
    elif user == 3:
        # This function is currently unavalible
        # but would allow the user to checkout books
        print('Checkout a Book')
    elif user == 4:
        # This function is currently unavailibe
        # but would allow the user to return books
        print('Return a Book')
    elif user == 5:
        # This fundtion is currently unavailble
        # but would allow the user to see overdue books
        print('View Overdue Books')
    elif user == 6:
        print('Exiting program. . .')
    else:
        print('That is an invalid Input')
    
    return user

if __name__ == "__main__":
    # You can use this space to test your functions
    user = 0
    
    while user != 6:
        display_menu()
        user = user_selection()
        
    pass

