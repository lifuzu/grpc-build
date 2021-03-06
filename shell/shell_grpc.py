# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: shell/shell.proto
# plugin: grpclib.plugin.main
import abc

import grpclib.const
import grpclib.client

import proto.messages.argument_pb2
import proto.messages.output_pb2
import shell.shell_pb2


class ShellBase(abc.ABC):

    @abc.abstractmethod
    async def Command(self, stream):
        pass

    def __mapping__(self):
        return {
            '/services.Shell/Command': grpclib.const.Handler(
                self.Command,
                grpclib.const.Cardinality.UNARY_UNARY,
                proto.messages.argument_pb2.Argument,
                proto.messages.output_pb2.Output,
            ),
        }


class ShellStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Command = grpclib.client.UnaryUnaryMethod(
            channel,
            '/services.Shell/Command',
            proto.messages.argument_pb2.Argument,
            proto.messages.output_pb2.Output,
        )
