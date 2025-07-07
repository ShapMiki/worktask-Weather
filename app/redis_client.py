import aioredis

redis = None

async def init_redis():
    global redis
    redis = await aioredis.from_url("redis://localhost:6379", encoding="utf-8", decode_responses=True)

async def close_redis():
    if redis:
        await redis.close()

async def get_redis():
    return redis