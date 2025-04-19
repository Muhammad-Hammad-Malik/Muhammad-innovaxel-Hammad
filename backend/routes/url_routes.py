from fastapi import APIRouter, HTTPException, status
from models.url_model import URLCreate, URLModel
from controllers.url_controller import create_short_url
from controllers.url_controller import get_original_url
from controllers.url_controller import update_short_url
from controllers.url_controller import delete_short_url_by_code
from controllers.url_controller import get_url_stats  
from models.url_model import URLUpdate

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


@router.put("/shorten/{short_code}", response_model=URLModel)
async def update_url(short_code: str, url_data: URLUpdate):
    try:
        updated_url = await update_short_url(short_code, url_data)
        return updated_url
    except ValueError as ve:
        raise HTTPException(status_code=404, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@router.delete("/shorten/{short_code}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_short_url(short_code: str):
    try:
        await delete_short_url_by_code(short_code)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Short URL not found: {str(e)}")


@router.get("/shorten/{short_code}/stats", response_model=URLModel)
async def get_stats(short_code: str):
    try:
        stats = await get_url_stats(short_code)
        return stats
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
