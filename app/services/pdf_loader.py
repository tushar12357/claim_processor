import fitz
import easyocr
import numpy as np
from PIL import Image
import io
from concurrent.futures import ThreadPoolExecutor

# Initialize ONCE (important)
reader = easyocr.Reader(['en'], gpu=False)


def process_page(page):
    try:
        # 1. Try normal text extraction first (FAST)
        text = page.get_text()
        if text.strip():
            return text

        # 2. Fallback to OCR (only if needed)
        pix = page.get_pixmap(matrix=fitz.Matrix(1, 1))  # low resolution (FAST)
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))

        img_np = np.array(image)

        results = reader.readtext(img_np, detail=0, paragraph=True)
        return " ".join(results)

    except Exception as e:
        return ""


def load_pdf(file_bytes):
    doc = fitz.open(stream=file_bytes, filetype="pdf")

    # 🔥 Parallel processing (FAST)
    with ThreadPoolExecutor() as executor:
        pages = list(executor.map(process_page, doc))

    return pages