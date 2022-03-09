class QuoteModel:
    """Class that represents a quote,
    Each quote has a body and an author."""

    def __init__(self, body="", author=""):
        """Creates a new 'Quote'."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a computer-readable string representation of this object."""
        return f"{self.body} - {self.author}"
