from aiohttp import web
import time 

@web.middleware
async def logger_middleware(request, handler):

    start = time.time()
    print(f"{request.method}, {request.path}")

    response = await handler(request)

    latency = round((time.time() - start) * 1000, 2)
    print(f"{response.status}, {latency}ms")

    return response 