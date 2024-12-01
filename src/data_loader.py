from pathlib import Path
from typing import Final

class DataLoader:
    """Handles loading and validation of data files."""
    
    def __init__(self, base_path: Path) -> None:
        """Initialize DataLoader with base directory path."""
        self.base_path: Final[Path] = base_path
