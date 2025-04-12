class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}), ISBN: {self.isbn}"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "year": self.year, "isbn": self.isbn}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["year"], data["isbn"])
