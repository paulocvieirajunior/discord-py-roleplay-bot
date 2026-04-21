from redis.asyncio import Redis

from .config import settings

r = Redis.from_url(url=settings.REDIS_URL, decode_responses=True)
