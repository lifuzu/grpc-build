
import asyncio

from grpclib.client import Channel

from .xcodebuild_pb2 import Argument
from .xcodebuild_grpc import XcodeStub


async def main():
    loop = asyncio.get_event_loop()
    channel = Channel('127.0.0.1', 50051, loop=loop)
    stub = XcodeStub(channel)

    response = await stub.Build(Argument(args=['World', 'Work']))
    print(response)


if __name__ == '__main__':
    asyncio.run(main())
