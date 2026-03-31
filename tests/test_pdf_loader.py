import io
from app.services.pdf_loader import load_pdf


def test_load_pdf():
    # Minimal valid PDF bytes
    fake_pdf = b"%PDF-1.4\n1 0 obj\n<<>>\nendobj\ntrailer\n<<>>\n%%EOF"

    pages = load_pdf(fake_pdf)

    assert isinstance(pages, list)