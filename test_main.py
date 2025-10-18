import os
from main import is_valid_url, generate_qr_code

def test_valid_url():
    """Ensure valid URLs return True."""
    assert is_valid_url("https://www.njit.edu")
    assert is_valid_url("http://github.com")
    assert is_valid_url("https://example.org/path?query=test")

def test_invalid_url():
    """Ensure invalid URLs return False."""
    assert not is_valid_url("htp:/invalid")
    assert not is_valid_url("just-text")
    assert not is_valid_url("www.google")  # missing scheme

def test_generate_qr_code_returns_image(tmp_path):
    """Generate and save QR code to a temporary directory."""
    output_file = tmp_path / "test_qr.png"
    
    generate_qr_code("https://www.njit.edu", output_file)
    
    # Just check that the file was created
    assert output_file.exists(), "QR code file should exist"
    assert output_file.suffix == ".png"
    assert output_file.stat().st_size > 0, "QR code file should not be empty"
