# ================= BOOK CLASS =================
class Book:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status

    def display_info(self):
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {self.status}")
        print("---------------------------")


# ================= LIBRARY MANAGER CLASS =================
class LibraryManager:
    def __init__(self):
        self.book_list = []

    def add_book(self, new_book):
        self.book_list.append(new_book)
        print("Book added successfully!")

    def display_all(self):
        if len(self.book_list) == 0:
            print("No books in the library.")
            return

        print("\n===== BOOK LIST =====")

        for book in self.book_list:
            book.display_info()

    def borrow_book(self, book_id):
        for book in self.book_list:
            if book.book_id == book_id:

                if book.status == "Available":
                    book.status = "Borrowed"
                    print("Book borrowed successfully!")
                else:
                    print("This book is already borrowed.")

                return

        print("Book not found.")


# ================= MENU FUNCTION =================
def main():
    library = LibraryManager()

    while True:
        print("\n===== LIBRARY MANAGEMENT MENU =====")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Borrow a book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            new_book = Book(book_id, title, author)
            library.add_book(new_book)
        elif choice == "2":
            library.display_all()
        elif choice == "3":
            book_id = input("Enter Book ID to borrow: ")
            library.borrow_book(book_id)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


# ================= MAIN PROGRAM =================
main()