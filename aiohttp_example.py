"""
aiohttp is an asynchronous HTTP client and server framework built on top of Python's asyncio library. It allows you to build high-performance and scalable web applications with Python by utilizing non-blocking I/O and coroutines.

aiohttp supports both client-side and server-side development, providing a complete set of tools for building web applications. It includes an HTTP client that supports HTTP/1.1 and HTTP/2 protocols and supports WebSocket communication, allowing you to build real-time web applications.

On the server-side, aiohttp provides a web server that supports routing, middlewares, and template rendering, making it easy to build robust web applications with Python.

Overall, aiohttp is a powerful and flexible framework that allows developers to build fast and scalable web applications using Python and asyncio.
"""


"""
FastAPI is a modern, fast, web framework for building APIs with Python 3.7+ based on the standard Python type hints. It is designed to be easy to use and easy to learn, while also being fast and scalable.

FastAPI is built on top of the Starlette framework and the Pydantic library, which provides a fast and efficient data validation system. It is designed to be asynchronous from the ground up, leveraging Python's asyncio library to enable high performance and scalability.

One of the main features of FastAPI is its automatic documentation generation. FastAPI automatically generates an OpenAPI schema and interactive API documentation using the standard Swagger UI. This makes it easy for developers to quickly prototype and test their APIs.

FastAPI also includes many other features that make building APIs easier and faster, including fast data serialization, dependency injection, automatic request validation, and built-in support for OAuth2 authentication.

Overall, FastAPI is a modern and powerful framework for building high-performance and scalable APIs with Python.
"""

import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com/events') as resp:
            print("Status:", resp.status)
            print("Content-type:", resp.headers['content-type'])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
