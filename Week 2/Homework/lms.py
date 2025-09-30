class Book():
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available
    
    def borrowable(self):
        if self.available:
            self.available = False
            return True
        return False
    
    def return_book(self):
        self.available = True


class User():
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        if book.borrowable():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
            return True
        else:
            print(f"Sorry, '{book.title}' is not available")
            return False

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            print(f"{self.name} returned '{book.title}'")
            return True
        else:
            print(f"You haven't borrowed '{book.title}'")
            return False

    def show_borrowed_books(self):
        if not self.borrowed_books:
            print("You haven't borrowed any books.")
        else:
            print(f"\n{self.name}'s Borrowed Books:")
            print("-" * 30)
            for book in self.borrowed_books:
                print(f"  • ID: {book.book_id} | '{book.title}' by {book.author}")


class Library():
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library")

    def search_book(self, keyword):
        results = []
        keyword = keyword.lower()
        for book in self.books:
            if (keyword in book.title.lower() or 
                keyword in book.author.lower() or 
                keyword == str(book.book_id)):
                results.append(book)
        
        if results:
            print(f"\nFound {len(results)} book(s):")
            print("-" * 40)
            for book in results:
                status = "Available" if book.available else "Not Available"
                print(f"  ID: {book.book_id} | '{book.title}' by {book.author} [{status}]")
        else:
            print("No books found matching your search")
        
        return results

    def show_books(self):
        if not self.books:
            print("The library has no books.")
            return
        
        print("\n" + "=" * 40)
        print("ALL BOOKS IN LIBRARY")
        print("=" * 40)
        for book in self.books:
            status = "Yes" if book.available else "No"
            print(f"ID: {book.book_id:3} | '{book.title:30}' | Author: {book.author:15} | Available: {status}")
        print("=" * 40)
        return len(self.books)

    def show_total_books(self):
        return len(self.books)

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None


def display_menu():
    print("\n" + "=" * 30)
    print("LMS")
    print("=" * 30)
    print("1. Show all books")
    print("2. Search for a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Show my borrowed books")
    print("6. Add a new book to library")
    print("7. Exit")
    print("=" * 30)


def main():
    library = Library()
    book1 = Book(1, "1001 Nights", "George")
    book2 = Book(2, "1002 Nights", "I'm Newbie")
    book3 = Book(3, "1003 Nights", "J.R.R. ABC")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    user_name = input("Enter your name: ")
    user = User(1, user_name)
    
    print(f"\nWelcome to the Library, {user_name}!")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            library.show_books()
        
        elif choice == "2":
            keyword = input("Enter search keyword (title/author/ID): ").strip()
            library.search_book(keyword)
        
        elif choice == "3":
            try:
                book_id = int(input("Enter book ID to borrow: ").strip())
                book = library.get_book_by_id(book_id)
                if book:
                    user.borrow_book(book)
                else:
                    print("Book not found with that ID")
            except ValueError:
                print("Please enter a valid book ID (number)")
        
        elif choice == "4":
            try:
                book_id = int(input("Enter book ID to return: ").strip())
                book = library.get_book_by_id(book_id)
                if book:
                    user.return_book(book)
                else:
                    print("Book not found with that ID")
            except ValueError:
                print("Please enter a valid book ID (number)")
        
        elif choice == "5":
            user.show_borrowed_books()
        
        elif choice == "6":
            try:
                book_id = library.show_total_books() + 1
                print(f"Your new book's ID is: {library.show_total_books() + 1}")
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                new_book = Book(book_id, title, author)
                library.add_book(new_book)
            except ValueError:
                print("Please enter a valid book ID (number)")
        
        elif choice == "7":
            print(f"\nThank you for using the library")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()