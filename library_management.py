import json

# File to store books
data_file = "library.json"

# Load and save library
def load_library():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file, indent=4)

# Library data
library = load_library()

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "y"
    
    if title and author and genre and year.isdigit():
        library.append({
            "title": title,
            "author": author,
            "year": int(year),
            "genre": genre,
            "read": read_status
        })
        save_library(library)
        print(f"'{title}' added successfully!")
    else:
        print("Invalid input. Please enter all details correctly.")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    global library
    library = [book for book in library if book["title"].lower() != title.lower()]
    save_library(library)
    print(f"'{title}' removed!")

def search_books():
    search_by = input("Search by (title/author): ").strip().lower()
    if search_by not in ["title", "author"]:
        print("Invalid search type. Please choose 'title' or 'author'.")
        return
    
    query = input("Enter search query: ").strip().lower()
    results = [book for book in library if query in book[search_by].lower()]
    
    if results:
        print("Matching Books:")
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.")

def display_all_books():
    if library:
        print("Your Library:")
        for book in library:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No books found.")

def display_statistics():
    total = len(library)
    read = sum(1 for book in library if book["read"])
    percent = (read / total * 100) if total else 0
    print(f"Total books: {total}")
    print(f"Percentage read: {percent:.2f}%")

def main():
    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            display_all_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
