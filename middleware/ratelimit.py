import redis
from aiohttp import web

@web.middleware
async def rateLimit_middleware(request, handler):

    r = redis.Redis(host="localhost", port=6379, decode_responses=True)

    user_id = request["user"]["sub"]
    userSession = "user-session:" + user_id

    requestIncrement = r.incr(userSession)

    if requestIncrement == 1: 
        r.expire(userSession, 60)

    if requestIncrement >= 10: 
        return web.Response(status=429, text="Ratelimited")

    return await handler(request)