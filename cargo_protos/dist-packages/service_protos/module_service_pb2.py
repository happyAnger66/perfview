# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_protos/module_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service_protos/module_service.proto',
  package='service_manager',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#service_protos/module_service.proto\x12\x0fservice_manager\x1a\x1bgoogle/protobuf/empty.proto\"\xb1\x01\n\nModuleInfo\x12\x12\n\nrecord_cmd\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\n \x01(\x04\x12\x0b\n\x03pid\x18\x0f \x01(\x05\x12\x0c\n\x04ppid\x18\x10 \x01(\x05\x12\x0c\n\x04pgid\x18\x14 \x01(\x05\x12\x16\n\x0eroslaunch_pgid\x18\x15 \x01(\x05\x12-\n\x06status\x18\x1e \x01(\x0e\x32\x1d.service_manager.ModuleStatus\"H\n\x14ModuleInfoCollection\x12\x30\n\x0bmodule_info\x18\x01 \x03(\x0b\x32\x1b.service_manager.ModuleInfo*y\n\x0cModuleStatus\x12\x0c\n\x08M_UNKOWN\x10\x00\x12\r\n\tM_INITING\x10\x01\x12\x0e\n\nM_STARTING\x10\x02\x12\r\n\tM_RUNNING\x10\x03\x12\r\n\tM_CLOSING\x10\x04\x12\x0c\n\x08M_CLOSED\x10\x05\x12\x10\n\x0cM_RESTARTING\x10\x06\x32\xb6\x01\n\rModuleService\x12I\n\x10RecordModuleInfo\x12\x1b.service_manager.ModuleInfo\x1a\x16.google.protobuf.Empty\"\x00\x12Z\n\x17GetModuleInfoCollection\x12\x16.google.protobuf.Empty\x1a%.service_manager.ModuleInfoCollection\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_MODULESTATUS = _descriptor.EnumDescriptor(
  name='ModuleStatus',
  full_name='service_manager.ModuleStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='M_UNKOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M_INITING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M_STARTING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M_RUNNING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M_CLOSING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M_CLOSED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M_RESTARTING', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=339,
  serialized_end=460,
)
_sym_db.RegisterEnumDescriptor(_MODULESTATUS)

ModuleStatus = enum_type_wrapper.EnumTypeWrapper(_MODULESTATUS)
M_UNKOWN = 0
M_INITING = 1
M_STARTING = 2
M_RUNNING = 3
M_CLOSING = 4
M_CLOSED = 5
M_RESTARTING = 6



_MODULEINFO = _descriptor.Descriptor(
  name='ModuleInfo',
  full_name='service_manager.ModuleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_cmd', full_name='service_manager.ModuleInfo.record_cmd', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='service_manager.ModuleInfo.name', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='service_manager.ModuleInfo.timestamp', index=2,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pid', full_name='service_manager.ModuleInfo.pid', index=3,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ppid', full_name='service_manager.ModuleInfo.ppid', index=4,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pgid', full_name='service_manager.ModuleInfo.pgid', index=5,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='roslaunch_pgid', full_name='service_manager.ModuleInfo.roslaunch_pgid', index=6,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='service_manager.ModuleInfo.status', index=7,
      number=30, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=86,
  serialized_end=263,
)


_MODULEINFOCOLLECTION = _descriptor.Descriptor(
  name='ModuleInfoCollection',
  full_name='service_manager.ModuleInfoCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='module_info', full_name='service_manager.ModuleInfoCollection.module_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=265,
  serialized_end=337,
)

_MODULEINFO.fields_by_name['status'].enum_type = _MODULESTATUS
_MODULEINFOCOLLECTION.fields_by_name['module_info'].message_type = _MODULEINFO
DESCRIPTOR.message_types_by_name['ModuleInfo'] = _MODULEINFO
DESCRIPTOR.message_types_by_name['ModuleInfoCollection'] = _MODULEINFOCOLLECTION
DESCRIPTOR.enum_types_by_name['ModuleStatus'] = _MODULESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ModuleInfo = _reflection.GeneratedProtocolMessageType('ModuleInfo', (_message.Message,), {
  'DESCRIPTOR' : _MODULEINFO,
  '__module__' : 'service_protos.module_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.ModuleInfo)
  })
_sym_db.RegisterMessage(ModuleInfo)

ModuleInfoCollection = _reflection.GeneratedProtocolMessageType('ModuleInfoCollection', (_message.Message,), {
  'DESCRIPTOR' : _MODULEINFOCOLLECTION,
  '__module__' : 'service_protos.module_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.ModuleInfoCollection)
  })
_sym_db.RegisterMessage(ModuleInfoCollection)



_MODULESERVICE = _descriptor.ServiceDescriptor(
  name='ModuleService',
  full_name='service_manager.ModuleService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=463,
  serialized_end=645,
  methods=[
  _descriptor.MethodDescriptor(
    name='RecordModuleInfo',
    full_name='service_manager.ModuleService.RecordModuleInfo',
    index=0,
    containing_service=None,
    input_type=_MODULEINFO,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetModuleInfoCollection',
    full_name='service_manager.ModuleService.GetModuleInfoCollection',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_MODULEINFOCOLLECTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MODULESERVICE)

DESCRIPTOR.services_by_name['ModuleService'] = _MODULESERVICE

# @@protoc_insertion_point(module_scope)
