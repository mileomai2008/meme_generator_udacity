from .IngestorInterface import IngestorInterface
from .TXTIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Class to encapsulate and differentiate between different Subclasses."""
    ingestors = [DocxIngestor, CSVIngestor, TextIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path):
        """Parse data by calling the correct class depending on
        the file extension in the variable path."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
