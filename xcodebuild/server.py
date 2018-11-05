
import subprocess

from proto.messages.output_pb2 import Output
from .xcodebuild_grpc import XcodeBase


def run_command(cmds: list) -> [int, str, str]:
    '''Run command with `cmds` as a list, for example: ['ls', '-l']
    '''
    proc = subprocess.run(cmds, capture_output=True)
    return proc.returncode, proc.stdout, proc.stderr

def run_xcodebuild(args: list) -> [int, str, str]:
    '''Run xcodebuild with some args
    '''
    cmds = ['xcodebuild']
    cmds.extend(args)
    return run_command(cmds)

def run_xcodeselect(args: list) -> [int, str, str]:
    '''Run xcodeselect with some args
    '''
    cmds = ['xcode-select']
    cmds.extend(args)
    return run_command(cmds)

class Xcode(XcodeBase):
    async def Build(self, stream):
        request = await stream.recv_message()

        retcode, stdout, stderr = run_xcodebuild(request.args)

        await stream.send_message(Output(retcode=retcode, stdout=stdout, stderr=stderr))

    async def Select(self, stream):
        request = await stream.recv_message()

        retcode, stdout, stderr = run_xcodeselect(request.args)

        await stream.send_message(Output(retcode=retcode, stdout=stdout, stderr=stderr))
