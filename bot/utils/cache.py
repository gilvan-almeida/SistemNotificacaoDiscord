from cachetools import TTLCache

userCache = TTLCache(maxsize=100, ttl=600)
taskCache = TTLCache(maxsize=100, ttl=600)
secaoTaskCache = TTLCache(maxsize=100, ttl=600)