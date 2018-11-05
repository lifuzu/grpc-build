# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shell/shell.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.messages import argument_pb2 as proto_dot_messages_dot_argument__pb2
from proto.messages import output_pb2 as proto_dot_messages_dot_output__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='shell/shell.proto',
  package='services',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11shell/shell.proto\x12\x08services\x1a\x1dproto/messages/argument.proto\x1a\x1bproto/messages/output.proto2(\n\x05Shell\x12\x1f\n\x07\x43ommand\x12\t.Argument\x1a\x07.Output\"\x00\x62\x06proto3')
  ,
  dependencies=[proto_dot_messages_dot_argument__pb2.DESCRIPTOR,proto_dot_messages_dot_output__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SHELL = _descriptor.ServiceDescriptor(
  name='Shell',
  full_name='services.Shell',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=91,
  serialized_end=131,
  methods=[
  _descriptor.MethodDescriptor(
    name='Command',
    full_name='services.Shell.Command',
    index=0,
    containing_service=None,
    input_type=proto_dot_messages_dot_argument__pb2._ARGUMENT,
    output_type=proto_dot_messages_dot_output__pb2._OUTPUT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SHELL)

DESCRIPTOR.services_by_name['Shell'] = _SHELL

# @@protoc_insertion_point(module_scope)
