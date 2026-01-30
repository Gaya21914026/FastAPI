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

