import redis

redis_client = redis.Redis.from_url("redis://127.0.0.1:6379", decode_responses=True)

redis_client.set("test_key", "Hello, Redis!")
value = redis_client.get("test_key")

print("Значення ключа:", value)
