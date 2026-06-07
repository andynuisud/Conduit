import aiohttp
import json
from aiohttp import web
from middleware.auth import auth_middleware
from middleware.ratelimit import rateLimit_middleware

async def handle(request):
    async with aiohttp.ClientSession() as session: 
        async with session.get("http://httpbin.org/get") as response: 
            data = await response.json()
            
            return web.Response(
                text=json.dumps(data, indent=2),
                content_type="application/json"
            )

app = web.Application(middlewares=[auth_middleware, rateLimit_middleware])
app.add_routes([web.get('/', handle)])

if __name__ == "__main__":
    web.run_app(app)