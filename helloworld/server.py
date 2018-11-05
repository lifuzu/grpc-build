
from .helloworld_pb2 import HelloReply
from .helloworld_grpc import GreeterBase


class Greeter(GreeterBase):
    async def SayHello(self, stream):
        request = await stream.recv_message()
        message = 'Hello {}!'.format(request.name)
        await stream.send_message(HelloReply(message=message))
