import random
import string
from datetime import datetime
from models.url_model import URLModel, URLCreate
from database import db


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
