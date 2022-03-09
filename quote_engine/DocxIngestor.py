import docx
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class DocxIngestor(IngestorInterface):
    """Docx child class it uses Document source files to return Quotes."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path):
        """Parse doc file given in the path variable
                to list quotes ."""
        doc = docx.Document(path)
        quotes = []
        for line in doc.paragraphs:
            line.text and quotes.append(
                QuoteModel(*line.text.split(" - ")))
        return quotes
