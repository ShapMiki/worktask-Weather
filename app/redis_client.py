import aioredis
from app.config import settings

redis = None

async def init_redis():
    global redis
    redis = await aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf-8", decode_responses=True)

async def close_redis():
    if redis:
        await redis.close()

async def get_redis():
    return redis