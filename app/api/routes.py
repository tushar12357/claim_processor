from fastapi import APIRouter, UploadFile, File, Form
from app.services.pdf_loader import load_pdf
from app.graph.builder import graph

router = APIRouter()

@router.post("/process")
async def process_claim(
    claim_id: str = Form(...),
    file: UploadFile = File(...)
):
    file_bytes = await file.read()
    pages = load_pdf(file_bytes)

    result = graph.invoke({
        "pages": pages
    })

    return {
        "claim_id": claim_id,
        "data": result.get("final_output", {})
    }