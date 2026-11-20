import redis.asyncio as redis

from settings import settings

class RedisClient:
    def __init__(self):
        self.redis = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_INTERNAL_PORT,
        password=settings.REDIS_PASSWORD,
        username=settings.REDIS_USERNAME,
        )

    async def set_cache(self, key: str, value: str | int, ttl: int) -> None:
        await self.redis.setex(key, ttl, value)

    async def get_cache(self, key: str):
        return await self.redis.get(key)

    async def delete_cache(self, key: str):
        await self.redis.delete(key)


redis_client = RedisClient()
