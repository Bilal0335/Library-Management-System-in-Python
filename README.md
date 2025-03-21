# Library Management System

This is a simple **Library Management System** that allows users to manage their book collection. Users can add, remove, search, and display books while also keeping track of their reading progress.

## Features

- 📚 **Add Books**: Store book details including title, author, year, genre, and read status.
- 🗑️ **Remove Books**: Remove books by title.
- 🔍 **Search Books**: Search for books by title or author.
- 📖 **Display All Books**: View all stored books with their details.
- 📊 **Statistics**: Track the percentage of books read.
- 💾 **Data Persistence**: Stores data in a JSON file (`library.json`).

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/your-username/library-management.git
   cd library-management
   ```
2. **Ensure Python is installed** (version 3.x recommended).
3. **Run the script**:
   ```bash
   python library.py
   ```

## Usage

1. Run the script and follow the on-screen menu.
2. Select an option:
   - `1` ➜ Add a new book.
   - `2` ➜ Remove a book by title.
   - `3` ➜ Search for a book by title or author.
   - `4` ➜ Display all books.
   - `5` ➜ Show reading statistics.
   - `6` ➜ Exit the program.

## Example

```
Menu
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
Enter your choice: 1
Enter the book title: The Great Gatsby
Enter the author: F. Scott Fitzgerald
Enter the publication year: 1925
Enter the genre: Fiction
Have you read this book? (yes/no): yes
'"The Great Gatsby" added successfully!'
```

## Future Improvements

- ✅ Implement a **GUI version** using Tkinter or PyQt.
- ✅ Add **book rating and reviews**.
- ✅ Enable **book categories and sorting**.
- ✅ Introduce **user authentication** for multiple users.

## License

This project is open-source and available under the [MIT License](LICENSE). Feel free to modify and improve it! 🚀
