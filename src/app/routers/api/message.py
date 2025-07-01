from fastapi import APIRouter, Depends

router = APIRouter()

@router.post('api/webhook/new_message')
async def new_message():
    pass