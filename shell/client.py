import asyncio

from grpclib.client import Channel

# from .shell_pb2 import Argument
from proto.messages.argument_pb2 import Argument
from .shell_grpc import ShellStub


async def main() -> int:
    loop = asyncio.get_event_loop()
    channel = Channel('127.0.0.1', 50051, loop=loop)
    stub = ShellStub(channel)

    response = await stub.Command(Argument(args=['ls', '-l']))
    print(response.stdout)
    if response.stderr:
        print(response.stderr)

    return response.retcode


if __name__ == '__main__':
    asyncio.run(main())