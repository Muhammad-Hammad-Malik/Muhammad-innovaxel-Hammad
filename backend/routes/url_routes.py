from fastapi import APIRouter, HTTPException, status
from models.url_model import URLCreate, URLModel
from controllers.url_controller import create_short_url

router = APIRouter()

@router.post("/shorten", response_model=URLModel, status_code=status.HTTP_201_CREATED)
async def shorten_url(url_data: URLCreate):
    print(url_data)
    try:
        new_url = await create_short_url(url_data)
        return new_url
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

