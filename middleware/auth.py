import jwt 
from aiohttp import web 

secretKey = "mysupersecretkey123456789"

@web.middleware
async def auth_middleware(request, handler):

    header = request.headers.get("Authorization")

    if header: 
        encoded_JWT = header.split(" ")[1]
    else:
        return web.Response(status=401, text="Unauthorized")

    try: 
        decoded_JWT = jwt.decode(encoded_JWT, secretKey, algorithms=["HS256"])
    except jwt.InvalidTokenError: 
        return web.Response(status=401, text="Unauthorized")

    user_id = request['user']['sub']

    return await handler(request)