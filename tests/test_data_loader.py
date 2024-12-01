from pathlib import Path
import pytest
from src.data_loader import DataLoader, DataValidationError

@pytest.fixture
def data_loader() -> DataLoader:
    """Fixture providing an instance of our DataLoader object."""
    return DataLoader(Path("data"))

def test_data_loader_initialization(data_loader: DataLoader) -> None:
    """Test DataLoader initialization with valid directory."""
    assert data_loader.base_path.exists(), "Data directory should exist"
    assert data_loader.base_path.is_dir(), "Data path should be a directory"
