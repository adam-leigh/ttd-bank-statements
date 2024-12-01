from pathlib import Path
from typing import Final

class DataValidationError(Exception):
    pass

class DataLoader:
    """Handles loading and validation of data files."""
    
    def __init__(self, base_path: Path) -> None:
        """Initialize DataLoader with base directory path."""
        self.base_path: Final[Path] = base_path
        self.raw_path: Final[Path] = self.base_path / "raw"
