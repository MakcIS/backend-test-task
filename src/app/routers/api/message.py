from fastapi import APIRouter, Security, HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.app.schemas.message import Message
from src.core.usecases.message import MessageUseCase, get_message_usecase, InvalidBotToken, ChannelNotFound

router = APIRouter()
security = HTTPBearer()

@router.post("/api/webhook/new_message", status_code=200)
async def new_message(message:Message,
                      credentials: HTTPAuthorizationCredentials = Security(security),
                      uc: MessageUseCase = Depends(get_message_usecase)):
    try:
        await uc.execute(token=credentials.credentials, message=message)
    except InvalidBotToken:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid bot token")
    except ChannelNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bot is not listening on any channel")
