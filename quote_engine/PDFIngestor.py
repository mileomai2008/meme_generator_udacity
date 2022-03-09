import os
import subprocess
from .IngestorInterface import IngestorInterface
from .TXTIngestor import TextIngestor


class PDFIngestor(IngestorInterface):
    """PDF child class it uses pdf source files to return Quotes."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path):
        """Parse pdf file given in the path variable
                to list quotes objects."""
        temp_text_file = './temp.txt'
        subprocess.call(['pdftotext', '-layout', path, temp_text_file])
        quotes = TextIngestor.parse(temp_text_file)
        os.remove(temp_text_file)
        return quotes
