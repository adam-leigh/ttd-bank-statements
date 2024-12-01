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

def test_raw_directory_exists(data_loader: DataLoader) -> None:
    """Test that raw data directory exists."""
    assert data_loader.raw_path.exists(), "Raw data directory should exist"
    assert data_loader.raw_path.is_dir(), "Raw data path should be a directory"

def test_processing_directories_exist(data_loader: DataLoader) -> None:
    """Test that processing directories exist."""
    assert data_loader.processed_path.exists(), "Processed directory should exist"
    assert data_loader.interim_path.exists(), "Interim directory should exist"
    assert data_loader.schemas_path.exists(), "Schemas directory should exist"
