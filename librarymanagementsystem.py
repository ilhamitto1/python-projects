import sys

# ===== OOP: Inheritance və Polymorphism üçün əsas sinif =====
class User:
    def action(self):
        print("User is doing something...")

class Student(User):  # Inheritance: Student <- User
    def action(self):
        print("Student is requesting a book.")

    def requestBook(self):
        print("Enter the name of the book you would like to check out:")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you want to return:")
        self.book = input()
        return self.book

class Admin(User):  # Inheritance: Admin <- User
    def action(self):
        print("Admin is adding books or managing inventory.")

# ===== Library sinifi: Encapsulation + Class/Object prinsipini daşıyır =====
class Library:
    def __init__(self, listofbooks):
        self.availablebooks = listofbooks  # Encapsulation

    def displayAvailablebooks(self):
        print("\nThe books we have in our library are:")
        for book in self.availablebooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availablebooks:
            print("You have now borrowed the book.")
            self.availablebooks.remove(requestedBook)
        else:
            print("Sorry, it is not available in the library.")

    def addBook(self, returnedBook):
        self.availablebooks.append(returnedBook)
        print("Thanks for returning the book.")

# ===== Main Proqram =====
def main():
    library = Library(["The Last Battle", "The Screwtape Letters", "The Great Divorce"])
    user = Student()  # Polymorphism: istəsək Admin də edə bilərik
    done = False

    while not done:
        print("""
======== LIBRARY MENU ========
1. Display all available books
2. Request a book
3. Return a book
4. Exit
""")
        try:
            choice = int(input("Enter a choice: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if choice == 1:
            library.displayAvailablebooks()
        elif choice == 2:
            library.lendBook(user.requestBook())
        elif choice == 3:
            library.addBook(user.returnBook())
    # Polymorphism burada işləyir
        elif choice == 4:
            sys.exit()
        else:
            print("Invalid choice. Try again.")

main()
