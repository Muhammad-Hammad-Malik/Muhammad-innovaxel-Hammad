import random
import string
from datetime import datetime
from models.url_model import URLModel, URLCreate
from database import db
from models.url_model import URLUpdate

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

async def create_short_url(data: URLCreate):
    urls_collection = db["urls"]
    # Generate a short code
    short_code = generate_short_code()
    now = datetime.utcnow()
    url_doc = {
        "_id": short_code,  # Use shortCode as the unique _id field
        "url": str(data.url),
        "shortCode": short_code,
        "createdAt": now,
        "updatedAt": now,
        "accessCount": 0
    }
    # Insert the new URL document
    try:
        result = await urls_collection.insert_one(url_doc)
    except Exception as e:
        print("error",e)
    # Fetch the inserted document
    new_url = await urls_collection.find_one({"_id": result.inserted_id})

    return URLModel(**new_url)

async def get_original_url(short_code: str):
    urls_collection = db["urls"]
    updated_doc = await urls_collection.find_one_and_update(
        {"_id": short_code},
        {"$inc": {"accessCount": 1}, "$set": {"updatedAt": datetime.utcnow()}},
        return_document=True  
    )
    if updated_doc:
        return URLModel(**updated_doc)
    return None


async def update_short_url(short_code: str, data: URLUpdate):
    urls_collection = db["urls"]
    existing_url = await urls_collection.find_one({"_id": short_code})
    
    if not existing_url:
        raise ValueError("Short URL not found")

    now = datetime.utcnow()
    update_result = await urls_collection.update_one(
        {"_id": short_code},
        {"$set": {"url": str(data.url), "updatedAt": now}}
    )

    # Fetch the updated document
    updated_url = await urls_collection.find_one({"_id": short_code})
    return URLModel(**updated_url)

async def delete_short_url_by_code(short_code: str):
    urls_collection = db["urls"]
    # Check if the short URL exists
    existing_url = await urls_collection.find_one({"_id": short_code})

    if not existing_url:
        raise ValueError("Short URL not found")

    # Delete the URL document
    await urls_collection.delete_one({"_id": short_code})
    
async def get_url_stats(short_code: str):
    urls_collection = db["urls"]
    url_doc = await urls_collection.find_one({"_id": short_code})
    if not url_doc:
        raise Exception("Short URL not found")
    return URLModel(**url_doc)
