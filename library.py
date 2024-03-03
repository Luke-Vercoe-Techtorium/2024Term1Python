class Book:
    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre

def main() -> None:
    id = 0
    books: dict[int, Book] = {}
    while True:
        operation = input("Enter an operation (add, display, search): ")
        operation = operation.strip()
        if operation == "add":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            genre = input("Enter the book genre: ")
            book = Book(title.strip(), author.strip(), genre.strip())
            books[id] = book
            print(f"Inserted the book with id {id}")
            id += 1
            print()
        elif operation == "display":
            for id in books:
                print(f"Id: {id}")
                print(f"Title: {books[id].title}")
                print(f"Author: {books[id].author}")
                print(f"Genre: {books[id].genre}")
                print()
        elif operation == "search":
            title = input("Enter the book title to search for: ")
            for id in books:
                if title in books[id].title:
                    print("Found Book:")
                    print(f"Id: {id}")
                    print(f"Title: {books[id].title}")
                    print(f"Author: {books[id].author}")
                    print(f"Genre: {books[id].genre}")
                    print()
        else:
            print("Please enter a valid operation")

if __name__ == "__main__":
    main()
