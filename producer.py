import random

import redis

redis_client = redis.Redis()

with redis.Redis() as redis_client:
    redis_client.lpush("queue", random.randint(0,100))


