import tkinter as tk
from tkinter import messagebox
import datetime

class LibraryItem:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category
        self.checked_out = False
        self.due_date = None

    def checkout(self, days=14):
        if not self.checked_out:
            self.checked_out = True
            self.due_date = datetime.datetime.now() + datetime.timedelta(days=days)
            return f"Checked out: {self.title}. Due on {self.due_date.date()}"
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            overdue_days = (datetime.datetime.now() - self.due_date).days
            self.due_date = None
            if overdue_days > 0:
                fine = overdue_days * 2  # $2 per overdue day
                return f"{self.title} is overdue. You owe a fine of ${fine}"
            else:
                return f"{self.title} returned on time."
        else:
            return f"{self.title} is not checked out."

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, title, author, category):
        item = LibraryItem(title, author, category)
        self.items.append(item)

    def search_by_title(self, title):
        return [item for item in self.items if item.title.lower() == title.lower()]

    def search_by_author(self, author):
        return [item for item in self.items if item.author.lower() == author.lower()]

    def search_by_category(self, category):
        return [item for item in self.items if item.category.lower() == category.lower()]

# GUI Setup
class LibraryGUI:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x400")

        # Add new item frame
        self.add_frame = tk.LabelFrame(self.root, text="Add New Item")
        self.add_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.title_label = tk.Label(self.add_frame, text="Title:")
        self.title_label.grid(row=0, column=0, padx=10, pady=5)
        self.title_entry = tk.Entry(self.add_frame)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        self.author_label = tk.Label(self.add_frame, text="Author:")
        self.author_label.grid(row=1, column=0, padx=10, pady=5)
        self.author_entry = tk.Entry(self.add_frame)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5)

        self.category_label = tk.Label(self.add_frame, text="Category:")
        self.category_label.grid(row=2, column=0, padx=10, pady=5)
        self.category_entry = tk.Entry(self.add_frame)
        self.category_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self.add_frame, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, columnspan=2, padx=10, pady=5)

        # Search frame
        self.search_frame = tk.LabelFrame(self.root, text="Search Library")
        self.search_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.search_entry = tk.Entry(self.search_frame, width=40)
        self.search_entry.grid(row=0, column=0, padx=10, pady=5)

        self.search_title_button = tk.Button(self.search_frame, text="Search by Title", command=self.search_by_title)
        self.search_title_button.grid(row=1, column=0, padx=10, pady=5)

        self.search_author_button = tk.Button(self.search_frame, text="Search by Author", command=self.search_by_author)
        self.search_author_button.grid(row=1, column=1, padx=10, pady=5)

        self.search_category_button = tk.Button(self.search_frame, text="Search by Category", command=self.search_by_category)
        self.search_category_button.grid(row=1, column=2, padx=10, pady=5)

        # Checkout & Return frame
        self.checkout_frame = tk.LabelFrame(self.root, text="Checkout/Return Item")
        self.checkout_frame.pack(fill="both", expand="yes", padx=10, pady=10)

        self.checkout_entry = tk.Entry(self.checkout_frame, width=40)
        self.checkout_entry.grid(row=0, column=0, padx=10, pady=5)

        self.checkout_button = tk.Button(self.checkout_frame, text="Checkout", command=self.checkout_item)
        self.checkout_button.grid(row=1, column=0, padx=10, pady=5)

        self.return_button = tk.Button(self.checkout_frame, text="Return", command=self.return_item)
        self.return_button.grid(row=1, column=1, padx=10, pady=5)

    def add_item(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        category = self.category_entry.get()
        if title and author and category:
            self.library.add_item(title, author, category)
            messagebox.showinfo("Success", f"Added: {title} by {author}")
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields are required.")

    def search_by_title(self):
        title = self.search_entry.get()
        results = self.library.search_by_title(title)
        self.display_results(results)

    def search_by_author(self):
        author = self.search_entry.get()
        results = self.library.search_by_author(author)
        self.display_results(results)

    def search_by_category(self):
        category = self.search_entry.get()
        results = self.library.search_by_category(category)
        self.display_results(results)

    def checkout_item(self):
        title = self.checkout_entry.get()
        results = self.library.search_by_title(title)
        if results:
            item = results[0]
            messagebox.showinfo("Checkout", item.checkout())
        else:
            messagebox.showerror("Error", "Item not found.")

    def return_item(self):
        title = self.checkout_entry.get()
        results = self.library.search_by_title(title)
        if results:
            item = results[0]
            messagebox.showinfo("Return", item.return_item())
        else:
            messagebox.showerror("Error", "Item not found.")

    def display_results(self, results):
        if results:
            result_str = "\n".join([f"{item.title} by {item.author} - {item.category}" for item in results])
            messagebox.showinfo("Search Results", result_str)
        else:
            messagebox.showinfo("Search Results", "No items found.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()
