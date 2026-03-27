class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"[{self.book_id}] '{self.title}' by {self.author} | Genre: {self.genre} | Status: {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Book '{book.title}' added successfully.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"🗑️ Book '{book.title}' removed successfully.")
                return
        print("❌ Book not found.")

    def search_book(self, keyword):
        results = [b for b in self.books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]
        if results:
            print(f"\n🔍 Search results for '{keyword}':")
            for book in results:
                print(" ", book)
        else:
            print("❌ No books found.")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    print(f"⚠️ '{book.title}' is already issued.")
                else:
                    book.is_issued = True
                    print(f"📤 '{book.title}' issued successfully.")
                return
        print("❌ Book not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    print(f"⚠️ '{book.title}' was not issued.")
                else:
                    book.is_issued = False
                    print(f"📥 '{book.title}' returned successfully.")
                return
        print("❌ Book not found.")

    def display_all_books(self):
        if not self.books:
            print("📭 No books in the library.")
        else:
            print(f"\n📚 Books in {self.name}:")
            for book in self.books:
                print(" ", book)

    def save_to_file(self, filename="library_records.txt"):
        with open(filename, "w") as f:
            f.write(f"Library: {self.name}\n")
            f.write("=" * 50 + "\n")
            for book in self.books:
                f.write(str(book) + "\n")
        print(f"💾 Records saved to '{filename}'.")


# ---- Main Menu ----
def main():
    library = Library("City Public Library")

    # Adding some sample books
    library.add_book(Book(1, "Python Crash Course", "Eric Matthes", "Programming"))
    library.add_book(Book(2, "The Alchemist", "Paulo Coelho", "Fiction"))
    library.add_book(Book(3, "Atomic Habits", "James Clear", "Self-Help"))
    library.add_book(Book(4, "Clean Code", "Robert C. Martin", "Programming"))

    # Rom-Com Books
    library.add_book(Book(5, "Twisted Love", "Ana Huang", "Rom-Com"))
    library.add_book(Book(6, "Twisted Games", "Ana Huang", "Rom-Com"))
    library.add_book(Book(7, "Twisted Hate", "Ana Huang", "Rom-Com"))
    library.add_book(Book(8, "Twisted Lies", "Ana Huang", "Rom-Com"))
    library.add_book(Book(9, "Too Good To Be True", "Prajakta Koli", "Rom-Com"))
    library.add_book(Book(10, "Mazedar Mushkil", "Prajakta Koli", "Rom-Com"))
    library.add_book(Book(11, "Rishtas and Red Flags", "Radhika Agarwal", "Rom-Com"))
    library.add_book(Book(12, "Love, Chaos & Calculus", "Radhika Agarwal", "Rom-Com"))

    while True:
        print("\n===== Library Management System =====")
        print("1. Display All Books")
        print("2. Add a Book")
        print("3. Remove a Book")
        print("4. Search Book")
        print("5. Issue a Book")
        print("6. Return a Book")
        print("7. Save Records to File")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":
            library.display_all_books()

        elif choice == "2":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            genre = input("Enter Genre: ")
            library.add_book(Book(book_id, title, author, genre))

        elif choice == "3":
            book_id = int(input("Enter Book ID to remove: "))
            library.remove_book(book_id)

        elif choice == "4":
            keyword = input("Enter title or author to search: ")
            library.search_book(keyword)

        elif choice == "5":
            book_id = int(input("Enter Book ID to issue: "))
            library.issue_book(book_id)

        elif choice == "6":
            book_id = int(input("Enter Book ID to return: "))
            library.return_book(book_id)

        elif choice == "7":
            library.save_to_file()

        elif choice == "8":
            print("👋 Goodbye!")
            print("please visit again😊")
            break

        else:
            print("⚠️ Invalid choice. Please enter between 1-8.")


if __name__ == "__main__":
    main()