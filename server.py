import asyncio

from grpclib.server import Server

from helloworld.server import Greeter
from xcodebuild.server import Xcode
from shell.server import Shell


async def serve(server, *, host='127.0.0.1', port=50051):
    await server.start(host, port)
    print('Serving on {}:{}'.format(host, port))
    try:
        await server.wait_closed()
    except asyncio.CancelledError:
        server.close()
        await server.wait_closed()


async def main():
    server = Server([
                    Greeter(),
                    Xcode(),
                    Shell()
                    ], loop=asyncio.get_event_loop())
    await serve(server)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
