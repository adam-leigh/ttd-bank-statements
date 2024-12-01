from pathlib import Path
from typing import Final, List, Literal

class DataValidationError(Exception):
    pass

class DataLoader:
    """Handles loading and validation of data files."""
    
    _ACCOUNT_PATTERNS: Final[dict[str, str]] = {
        "ops": "statement-03",
        "main": "statement-24"
    }
    
    def __init__(self, base_path: Path) -> None:
        """Initialize DataLoader with base directory path."""
        self.base_path: Final[Path] = base_path
        self.raw_path: Final[Path] = self.base_path / "raw"
        self.processed_path: Final[Path] = self.base_path / "processed"
        self.interim_path: Final[Path] = self.base_path / "interim"
        self.schemas_path: Final[Path] = self.base_path / "schemas"

    def get_bank_statements(self, account: Literal["ops", "main"]) -> List[Path]:
        """Get bank statements for specified account type."""
        pattern = self._ACCOUNT_PATTERNS[account]
        return list(filter(
            lambda p: p.name.startswith(pattern) and p.suffix in ('.csv', '.xlsx'),
            self.raw_path.iterdir()
        ))
