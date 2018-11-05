
from .xcodebuild_pb2 import Output
from .xcodebuild_grpc import XcodeBase


class Xcode(XcodeBase):
    async def Build(self, stream):
        request = await stream.recv_message()
        message = 'Hello {}!'.format(request.args)
        await stream.send_message(Output(retcode=2, stdout=message, stderr=""))
