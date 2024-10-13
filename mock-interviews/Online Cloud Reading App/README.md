# Online Cloud Reading App Mock Interview

## Problem Overview

Design a cloud-based reading application similar to Amazon Kindle for short stories. The app should allow users to manage a digital library, select active books, and track reading progress.

### Features:
- Users have a library of books they can add to or remove from.
- Users can set a book from their library as active.
- The app remembers where a user left off in a book.
- The app displays one page of text at a time in the active book.

### Classes:
- **Book**
    - Attributes: `id`, `title` (str), `pages` (list of strings, each representing a page), `last_active_page` (int)
    - Methods: Add or remove pages, update last active page.
  
- **Library**
    - Attributes: `books` (list of Book objects), `active_book` (Book object)
    - Methods: Add/remove books, set active book.

---

## Coding Challenges

### 1. **Search Functionality**:
- **Description**: Implement a method to search for books by title. Return details if found, or an appropriate message if not.
- **Hint**: Iterate through the dictionary of books and check if the title contains the search term (case-insensitive).

### 2. **Pagination Management**:
- **Description**: Implement a method that allows users to go to a specific page in the active book. Ensure that the page number is valid.
- **Hint**: Check that the requested page is within bounds.

### 3. **Bookmarking Pages**:
- **Description**: Implement a bookmarking feature that saves the current page of the active book. Provide a method to retrieve the bookmarked pages.

### 4. **Recommendations Based on Reading History**:
- **Description**: When a user finishes reading a book, suggest a new book based on genre or author.

### 5. **Sorting Books**:
- **Description**: Implement a method to sort books in the library either by title or by the number of pages. Allow users to choose the criterion.
- **Hint**: Use Python’s sorted() function with a custom key.

### **6. User Ratings**:
- **Description**: Add functionality for users to rate books. Store the ratings and calculate the average rating for each book.
- **Hint**: Store ratings as a list within each Book instance, and implement a method to compute the average.

7. Accessibility - Increase Font Size:
- **Description**: Allow users to increase the font size for reading. Implement a basic font size increase feature.
---

### Example Class Structure

```python
class Book:
    def __init__(self, id, title, pages):
        self.id = id
        self.title = title
        self.pages = pages
        self.last_active_page = 0

class Library:
    def __init__(self):
        self.books = {}
        self.active_book = None

    def add_book(self, book):
        self.books[book.id] = book

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]

    def set_active_book(self, book_id):
        if book_id in self.books:
            self.active_book = self.books[book_id]
