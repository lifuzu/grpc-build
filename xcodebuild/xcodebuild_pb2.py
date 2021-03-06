# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xcodebuild/xcodebuild.proto

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
  name='xcodebuild/xcodebuild.proto',
  package='services',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bxcodebuild/xcodebuild.proto\x12\x08services\x1a\x1dproto/messages/argument.proto\x1a\x1bproto/messages/output.proto2F\n\x05Xcode\x12\x1d\n\x05\x42uild\x12\t.Argument\x1a\x07.Output\"\x00\x12\x1e\n\x06Select\x12\t.Argument\x1a\x07.Output\"\x00\x62\x06proto3')
  ,
  dependencies=[proto_dot_messages_dot_argument__pb2.DESCRIPTOR,proto_dot_messages_dot_output__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_XCODE = _descriptor.ServiceDescriptor(
  name='Xcode',
  full_name='services.Xcode',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=101,
  serialized_end=171,
  methods=[
  _descriptor.MethodDescriptor(
    name='Build',
    full_name='services.Xcode.Build',
    index=0,
    containing_service=None,
    input_type=proto_dot_messages_dot_argument__pb2._ARGUMENT,
    output_type=proto_dot_messages_dot_output__pb2._OUTPUT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Select',
    full_name='services.Xcode.Select',
    index=1,
    containing_service=None,
    input_type=proto_dot_messages_dot_argument__pb2._ARGUMENT,
    output_type=proto_dot_messages_dot_output__pb2._OUTPUT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_XCODE)

DESCRIPTOR.services_by_name['Xcode'] = _XCODE

# @@protoc_insertion_point(module_scope)
