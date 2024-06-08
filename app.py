def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
        print(f"{package} is already installed.")
    except ImportError:
        print(f"{package} is not installed. Would you like to install it now? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            try:
                import sys
                import subprocess
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                importlib.import_module(package)
                print(f"{package} has been successfully installed.")
            except Exception as e:
                print(f"Failed to install {package} module: {e}")
                exit(1)
        else:
            print(f"Please install the {package} module to proceed.")
            exit(1)

# Ensure required modules are installed
modules = ["tkinter", "ttkbootstrap"]
for module in modules:
    install_and_import(module)

# Importing the necessary modules
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class BookManagementSystem:
    def __init__(self):
        self.books = [
            Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4"),
            Book("1984", "George Orwell", "978-0-452-28423-4"),
            Book("Pride and Prejudice", "Jane Austen", "978-0-19-953556-9"),
            Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5"),
            Book("Moby Dick", "Herman Melville", "978-0-14-243724-7"),
            Book("War and Peace", "Leo Tolstoy", "978-0-14-303999-0"),
            Book("Ulysses", "James Joyce", "978-0-679-72232-9"),
            Book("The Odyssey", "Homer", "978-0-14-026886-7"),
            Book("Madame Bovary", "Gustave Flaubert", "978-0-14-044912-9"),
            Book("The Divine Comedy", "Dante Alighieri", "978-0-14-243722-3"),
            Book("The Brothers Karamazov", "Fyodor Dostoevsky", "978-0-14-044924-2"),
            Book("Crime and Punishment", "Fyodor Dostoevsky", "978-0-14-044913-6"),
            Book("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0"),
            Book("Wuthering Heights", "Emily Bronte", "978-0-14-143955-6"),
            Book("Great Expectations", "Charles Dickens", "978-0-14-143956-3"),
        ]

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        return self.books

    def search_books(self, query):
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]

# Main application class
class BookManagementApp:
    def __init__(self, root):
        self.system = BookManagementSystem()
        self.root = root
        self.root.title("Book Management System")

        # Create the main container frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.place(relwidth=1, relheight=1)

        # Create and configure the notebook
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=BOTH, expand=1)

        # Create frames for each tab
        self.create_home_tab()
        self.create_add_book_tab()
        self.create_view_books_tab()
        self.create_search_books_tab()

    def create_home_tab(self):
        home_frame = ttk.Frame(self.notebook)
        self.notebook.add(home_frame, text="Home")

        home_label = ttk.Label(home_frame, text="Welcome to the Book Management System", font=("Arial", 16))
        home_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_add_book_tab(self):
        add_book_frame = ttk.Frame(self.notebook)
        self.notebook.add(add_book_frame, text="Add Book")

        title_label = ttk.Label(add_book_frame, text="Title:")
        title_label.grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = ttk.Entry(add_book_frame)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        author_label = ttk.Label(add_book_frame, text="Author:")
        author_label.grid(row=1, column=0, padx=10, pady=10)
        self.author_entry = ttk.Entry(add_book_frame)
        self.author_entry.grid(row=1, column=1, padx=10, pady=10)

        isbn_label = ttk.Label(add_book_frame, text="ISBN:")
        isbn_label.grid(row=2, column=0, padx=10, pady=10)
        self.isbn_entry = ttk.Entry(add_book_frame)
        self.isbn_entry.grid(row=2, column=1, padx=10, pady=10)

        add_button = ttk.Button(add_book_frame, text="Add Book", command=self.add_book, bootstyle=PRIMARY)
        add_button.grid(row=3, columnspan=2, pady=20)

    def create_view_books_tab(self):
        view_books_frame = ttk.Frame(self.notebook)
        self.notebook.add(view_books_frame, text="View Books")

        columns = ("title", "author", "isbn")
        self.books_treeview = ttk.Treeview(view_books_frame, columns=columns, show="headings")
        self.books_treeview.heading("title", text="Title")
        self.books_treeview.heading("author", text="Author")
        self.books_treeview.heading("isbn", text="ISBN")
        self.books_treeview.pack(fill=BOTH, expand=1)

        self.update_books_treeview()

    def create_search_books_tab(self):
        search_books_frame = ttk.Frame(self.notebook)
        self.notebook.add(search_books_frame, text="Search Books")

        search_label = ttk.Label(search_books_frame, text="Search Query:")
        search_label.grid(row=0, column=0, padx=10, pady=10)
        self.search_entry = ttk.Entry(search_books_frame)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)

        search_button = ttk.Button(search_books_frame, text="Search", command=self.search_books, bootstyle=PRIMARY)
        search_button.grid(row=1, columnspan=2, pady=10)

        self.search_results_treeview = ttk.Treeview(search_books_frame, columns=("title", "author", "isbn"), show="headings")
        self.search_results_treeview.heading("title", text="Title")
        self.search_results_treeview.heading("author", text="Author")
        self.search_results_treeview.heading("isbn", text="ISBN")
        self.search_results_treeview.grid(row=2, columnspan=2, pady=10)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()

        if title and author and isbn:
            new_book = Book(title, author, isbn)
            self.system.add_book(new_book)
            self.update_books_treeview()
            messagebox.showinfo("Success", "Book added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)

    def update_books_treeview(self):
        for row in self.books_treeview.get_children():
            self.books_treeview.delete(row)
        for book in self.system.view_books():
            self.books_treeview.insert("", tk.END, values=(book.title, book.author, book.isbn))

    def search_books(self):
        query = self.search_entry.get()
        results = self.system.search_books(query)
        for row in self.search_results_treeview.get_children():
            self.search_results_treeview.delete(row)
        for book in results:
            self.search_results_treeview.insert("", tk.END, values=(book.title, book.author, book.isbn))

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")
    app = BookManagementApp(root)
    root.mainloop()
