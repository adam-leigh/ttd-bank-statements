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

def test_get_bank_statements(data_loader: DataLoader) -> None:
    """Test getting bank statements by account type."""
    ops_statements = data_loader.get_bank_statements(account="ops")
    assert all(p.name.startswith('statement-03') for p in ops_statements)

    main_statements = data_loader.get_bank_statements(account="main")
    assert all(p.name.startswith('statement-24') for p in main_statements)

def test_check_statement_format(data_loader: DataLoader) -> None:
    """Test detection of statement format and cleaning requirements."""
    statements = data_loader.get_bank_statements(account="main")
    formats = data_loader.check_statement_formats(statements)
    
    # Formats should be a list of tuples: (Path, bool, bool)
    # First bool indicates if has headers, second bool indicates if needs cleaning
    assert all(len(f) == 3 and isinstance(f[1], bool) and isinstance(f[2], bool) 
              for f in formats), "Format info should contain path and two booleans"
              
    # Check specific cases based on content
    for statement_path, has_headers, needs_cleaning in formats:
        if not has_headers and needs_cleaning:
            # Verify files marked for cleaning actually need it
            file_content = data_loader.read_first_rows(statement_path)
            assert any('HIST' in row[0] for row in file_content), \
                   "Files marked for cleaning should contain HIST in first column"
