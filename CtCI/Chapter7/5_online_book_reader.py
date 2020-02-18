class User(object):
    def __init__(self, id, details, account_type):
        self._id = id
        self._details = details
        self._account_type = account_type

    # getter and setter
    @property
    def id(self): return self._id
    
    @id.setter
    def id(self, id): self._id = id

    @property
    def details(self): return self._details
    
    @details.setter
    def details(self, details): self._details = details

    @property
    def account_type(self): return self._account_type
    
    @account_type.setter
    def account_type(self, account_type): self._account_type = account_type


class UserManager(object):
    def __init__(self):
        self._users = {} # id -> user object

    def add(self, id, details, account_type):
        if id in self._users: return None
        user = User(id, details, account_type)
        self._users[id] = user
        return user

    def remove(self, data): # data: id or user object
        id = data.id if isinstance(id, User) else data
        if id in self._users:
            self._users.pop(id)
            return True
        else:
            return False

    def find(self, id):
        return self._users[id] if id in self._users else None

    
class Book(object):
    def __init__(self, id, details):
        self._id = id
        self._details = details

    # getter and setter
    @property
    def id(self): return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def details(self): return self._details

    @details.setter
    def details(self, details): self._details = details


class Library(object):
    def __init__(self):
        self._books = {} # id -> book object

    def add(self, id, details):
        if id in self._books: return None
        book = Book(id, details)
        self._books[id] = book
        return book

    def remove(self, data): # data: id or book object
        id = data.id if isinstance(data, Book) else data
        if id in self._books:
            self._books.pop(id)
            return True
        else:
            return False

    def find(self, id):
        return self._books[id] if id in self._books else None


class Display(object):
    def __init__(self):
        self._active_book = None
        self._active_user = None
        self._page_number = None

    def display_user(self, user):
        self._active_user = user
        self.refresh_username()

    def display_book(self, book):
        self._active_book = book
        self.refresh_title()
        self.refresh_details()
        self.refresh_page()

    def refresh_username(self):
        pass

    def refresh_title(self):
        pass

    def refresh_details(self):
        pass

    def refresh_page(self):
        pass

    def turn_page_forward(self):
        self._page_number += 1
        self.refresh_page()

    def turn_page_backward(self):
        self._page_number -= 1
        self.refresh_page()


class OnlineReaderSystem(object):
    def __init__(self):
        self._user_manager = UserManager()
        self._library = Library()
        self._display = Display()
        self._active_book = None
        self._active_user = None

    # getter and setter
    @property
    def book_manager(self): return self._book_manager
    
    @property
    def library(self): return self._library

    @property
    def display(self): return self._display

    @property
    def active_book(self): return self._active_book

    @active_book.setter
    def active_book(self, book): self._active_book = book

    @property
    def active_user(self): return self._active_user

    @active_user.setter
    def active_user(self, user): self._active_user = user

A = OnlineReaderSystem()
lib = A.library
lib.add(1, Book(1, "hoge"))
print(lib.find(1))
print(lib.find(2))
