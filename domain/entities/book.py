
from author import Author


class Book:
    def __init__(self, title: str, author: Author) -> None:
        self.title = title
        self.author = author
