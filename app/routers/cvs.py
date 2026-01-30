from fastapi import APIRouter,UploadFile
from fastapi import  UploadFile
from app.schemas.ai import ChatRequest,ChatResponse
from app.services.pdf import save,pdf_to_images
from app.services.ai import openrouter_chat

router = APIRouter( prefix="/cvs/upload",tags=["upload"])
@router.post("/")
def upload(Myfile:UploadFile):
    return save(Myfile)


@router.post("", response_model=ChatResponse)
async def chat_with_ai(data: ChatRequest): 
    ai_message = await openrouter_chat(data.message, data.role) 
    return ChatResponse(response=ai_message )

@router.post("/summarize_with_ia")
async def summarize_cv(file: UploadFile):
    
    result = save(file)
    images = result["images"]

    # 2. Prendre la première image
    first_image = images[0]

    # 3. Envoyer à l’IA
    summary = await openrouter_chat(
        message="que vois tu sur cette image?",
        image_path=first_image
    )

    return {"summary": summary}
