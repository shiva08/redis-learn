import redis

config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}

redisObject = redis.StrictRedis(**config)