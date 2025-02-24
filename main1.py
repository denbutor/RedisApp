import redis
import time
import random
from string import ascii_letters

redis_client = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
for key in redis_client.scan_iter('*ab', count=100):
    print(key, redis_client.get(key))
# gen = redis_client.scan_iter(match='*ab', count=100)
# while True:
#     print(next(gen))
# print(redis_client.keys('*'))
# redis_client.set('counter', 1)
#
# while True:
#     redis_client.set("".join(random.sample(ascii_letters, random.randint(1, 20))), 1)
#     print(f"Лічильник: {redis_client.get('counter')}")
#     time.sleep(1)
