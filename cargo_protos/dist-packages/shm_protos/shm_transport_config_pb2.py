# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shm_protos/shm_transport_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='shm_protos/shm_transport_config.proto',
  package='cargo',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%shm_protos/shm_transport_config.proto\x12\x05\x63\x61rgo\"G\n\x0bTopicConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nqueue_size\x18\x02 \x01(\x05\x12\x16\n\x0emsg_size_ratio\x18\x03 \x01(\x02\"M\n\x12ShmTransportConfig\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\"\n\x06\x63onfig\x18\n \x03(\x0b\x32\x12.cargo.TopicConfigb\x06proto3'
)




_TOPICCONFIG = _descriptor.Descriptor(
  name='TopicConfig',
  full_name='cargo.TopicConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cargo.TopicConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='queue_size', full_name='cargo.TopicConfig.queue_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg_size_ratio', full_name='cargo.TopicConfig.msg_size_ratio', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=119,
)


_SHMTRANSPORTCONFIG = _descriptor.Descriptor(
  name='ShmTransportConfig',
  full_name='cargo.ShmTransportConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='cargo.ShmTransportConfig.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='cargo.ShmTransportConfig.config', index=1,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=198,
)

_SHMTRANSPORTCONFIG.fields_by_name['config'].message_type = _TOPICCONFIG
DESCRIPTOR.message_types_by_name['TopicConfig'] = _TOPICCONFIG
DESCRIPTOR.message_types_by_name['ShmTransportConfig'] = _SHMTRANSPORTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TopicConfig = _reflection.GeneratedProtocolMessageType('TopicConfig', (_message.Message,), {
  'DESCRIPTOR' : _TOPICCONFIG,
  '__module__' : 'shm_protos.shm_transport_config_pb2'
  # @@protoc_insertion_point(class_scope:cargo.TopicConfig)
  })
_sym_db.RegisterMessage(TopicConfig)

ShmTransportConfig = _reflection.GeneratedProtocolMessageType('ShmTransportConfig', (_message.Message,), {
  'DESCRIPTOR' : _SHMTRANSPORTCONFIG,
  '__module__' : 'shm_protos.shm_transport_config_pb2'
  # @@protoc_insertion_point(class_scope:cargo.ShmTransportConfig)
  })
_sym_db.RegisterMessage(ShmTransportConfig)


# @@protoc_insertion_point(module_scope)
