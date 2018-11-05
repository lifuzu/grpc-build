import subprocess

from proto.messages.output_pb2 import Output
from .shell_grpc import ShellBase


def run_command(cmds: list) -> [int, str, str]:
    '''Run command with `cmds` as a list, for example: ['ls', '-l']
    '''
    proc = subprocess.run(cmds, capture_output=True)
    return proc.returncode, proc.stdout, proc.stderr

class Shell(ShellBase):
    async def Command(self, stream):
        request = await stream.recv_message()

        retcode, stdout, stderr = run_command(request.args)

        await stream.send_message(Output(retcode=retcode, stdout=stdout, stderr=stderr))
