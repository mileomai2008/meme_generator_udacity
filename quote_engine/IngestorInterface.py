from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Ingestor Interface to be inherited by different sub-Classes
    to ingest different types of data like DOCx,CSV,...etc."""
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Check if the file type is valid."""
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path):
        """Parse different types of data in children modules."""
        pass
