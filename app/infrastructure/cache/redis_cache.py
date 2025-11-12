import logging
from redis.asyncio import Redis

from config.config import settings

logger = logging.getLogger("Redis")

class RedisCli:
    """Base class for Redis client"""

    redis = Redis(
        host=settings.redis.HOST.get_secret_value(),
        port=settings.redis.PORT,
        db=settings.redis.DB,
    )

    timelimit = settings.redis.TTL

    async def test(self):
        try:
            pong = await self.redis.ping()
            if pong:
                logger.debug("Redis Started")
            else:
                raise ConnectionError("Redis ping returned False")

        except (ConnectionError, TimeoutError) as e:
            logger.error(f"Redis connection failed: {e}")
            raise RuntimeError("Redis is not responding") from e

        except Exception as e:
            logger.exception("Unexpected error while connecting to Redis")
            raise RuntimeError("Redis initialization failed") from e


redis_cli = RedisCli()
