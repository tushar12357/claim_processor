import fitz
import easyocr
import numpy as np
from PIL import Image
import io

reader = easyocr.Reader(['en'], gpu=False)

def load_pdf(file_bytes):
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    pages = []

    for page in doc:
        pix = page.get_pixmap()
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))

        # convert to numpy array
        img_np = np.array(image)

        # OCR
        results = reader.readtext(img_np, detail=0)

        text = "\n".join(results)
        pages.append(text)

    return pages