assert str(book) == "Book: 1984 by Orwell", f"got {str(book)!r}"
assert str(Book("Dune", "Herbert")) == "Book: Dune by Herbert", f"got {str(Book('Dune', 'Herbert'))!r}"
print("classes8 ✓")
