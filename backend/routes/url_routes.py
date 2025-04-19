from fastapi import APIRouter, HTTPException, status
from models.url_model import URLCreate, URLModel
from controllers.url_controller import create_short_url
from controllers.url_controller import get_original_url

router = APIRouter()

@router.post("/shorten", response_model=URLModel, status_code=status.HTTP_201_CREATED)
async def shorten_url(url_data: URLCreate):
    print(url_data)
    try:
        new_url = await create_short_url(url_data)
        return new_url
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/shorten/{short_code}", response_model=URLModel)
async def retrieve_original_url(short_code: str):
    url_data = await get_original_url(short_code)
    if not url_data:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return url_data
