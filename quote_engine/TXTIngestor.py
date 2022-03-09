from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    """TXT child class it uses text source files to return Quotes."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path):
        """Parse text file given in the path variable
                    to list quotes objects."""
        file = open(path, "r")
        quotes = []
        lines = file.readlines()
        file.close()
        for quote in lines:
            if len(quote.strip()) != 0:
                quotes.append(QuoteModel(*quote.rstrip("\n").split(" - ")))
        return quotes
