import redis
from params import REDIS_DB, REDIS_HOST, REDIS_PORT

database = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
