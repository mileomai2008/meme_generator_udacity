import pandas as pd
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """CSV child class it uses CSV source files to return Quotes."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path):
        """Parse CSV tables given in the path variable
        to list quotes objects."""
        csv = pd.read_csv(path)
        return [QuoteModel(f'"{row[0]}"', row[1])
                for index, row in csv.iterrows()]
