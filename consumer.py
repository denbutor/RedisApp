import random

import redis

redis_client = redis.Redis()

with redis.Redis() as redis_client:
    print("random number was: ", redis_client.brpop("queue"))


