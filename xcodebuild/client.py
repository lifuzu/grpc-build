
import asyncio

from grpclib.client import Channel

from .xcodebuild_pb2 import Argument
from .xcodebuild_grpc import XcodeStub


async def main() -> int:
    loop = asyncio.get_event_loop()
    channel = Channel('docker.for.mac.host.internal', 50051, loop=loop)
    stub = XcodeStub(channel)

    response = await stub.Build(Argument(args=['-help']))
    print(response.stdout)
    if response.stderr:
        print(response.stderr)

    response = await stub.Select(Argument(args=['-p']))
    print(response.stdout)
    if response.stderr:
        print(response.stderr)

    return response.retcode


if __name__ == '__main__':
    asyncio.run(main())
