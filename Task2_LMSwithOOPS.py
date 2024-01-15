class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.is_available:
                print(book)

    def borrow_book(self, member, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower() and book.is_available:
                member.borrowed_books.append(book)
                book.is_available = False
                print(f"\nBook '{book.title}' borrowed successfully by {member.name}.")
                return
        print(f"\nBook '{book_title}' not available for borrowing.")

    def return_book(self, member, book_title):
        for book in member.borrowed_books:
            if book.title.lower() == book_title.lower():
                book.is_available = True
                member.borrowed_books.remove(book)
                print(f"\nBook '{book.title}' returned successfully by {member.name}.")
                return
        print(f"\nBook '{book_title}' not borrowed by {member.name}.")

    def display_member_info(self, member):
        print(f"\nBorrowed Books by {member.name} (ID: {member.member_id}):")
        for book in member.borrowed_books:
            print(book)


def main():
    library = Library()

    while True:
        print("Welcome to Pragati Library Management System(LMS)")
        print("\nOptions:")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Display Available Books")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Display Member Information")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)
            print(f"\nBook '{title}' added to the library.")

        elif choice == '2':
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            new_member = Member(name, member_id)
            library.add_member(new_member)
            print(f"\nMember '{name}' added to the library.")

        elif choice == '3':
            library.display_available_books()

        elif choice == '4':
            member_id = input("Enter your member ID: ")
            book_title = input("Enter the title of the book you want to borrow: ")
            member = next((m for m in library.members if m.member_id == member_id), None)
            if member:
                library.borrow_book(member, book_title)
            else:
                print("\nMember not found. Please check your member ID.")

        elif choice == '5':
            member_id = input("Enter your member ID: ")
            book_title = input("Enter the title of the book you want to return: ")
            member = next((m for m in library.members if m.member_id == member_id), None)
            if member:
                library.return_book(member, book_title)
            else:
                print("\nMember not found. Please check your member ID.")

        elif choice == '6':
            member_id = input("Enter member ID to display information: ")
            member = next((m for m in library.members if m.member_id == member_id), None)
            if member:
                library.display_member_info(member)
            else:
                print("\nMember not found. Please check the member ID.")

        elif choice == '7':
            print("\nThank you for using the Library Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
