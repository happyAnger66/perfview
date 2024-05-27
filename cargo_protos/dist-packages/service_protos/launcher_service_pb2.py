# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_protos/launcher_service.proto
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
  name='service_protos/launcher_service.proto',
  package='service_manager',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%service_protos/launcher_service.proto\x12\x0fservice_manager\x1a\x1bgoogle/protobuf/empty.proto\"\x80\x01\n\rOneNodeStatus\x12\x0c\n\x04node\x18\x01 \x01(\t\x12+\n\x06status\x18\x02 \x01(\x0e\x32\x1b.service_manager.NodeStatus\x12\x0b\n\x03pid\x18\x03 \x01(\x05\x12\x0b\n\x03\x63md\x18\x04 \x01(\t\x12\x0b\n\x03log\x18\x05 \x01(\t\x12\r\n\x05group\x18\x06 \x01(\t\"K\n\x14NodeStatusCollection\x12\x33\n\x0bnode_status\x18\x01 \x03(\x0b\x32\x1e.service_manager.OneNodeStatus\"\x8b\x01\n\x0eNodeCollection\x12\r\n\x05nodes\x18\x01 \x03(\t\x12\x36\n\nnode_group\x18\x02 \x01(\x0e\x32\".service_manager.NodeGroupCategory\x12\x12\n\nsim_status\x18\x03 \x01(\x08\x12\x0c\n\x04\x61rgs\x18\x04 \x01(\t\x12\x10\n\x08identity\x18\x05 \x01(\t\"\x1d\n\nLogMessage\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"\x18\n\x06Option\x12\x0e\n\x06gflags\x18\x01 \x01(\t\"J\n\rOneOrinStatus\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x06status\x18\x02 \x01(\x0e\x32\x1b.service_manager.OrinStatus\"Z\n\x08\x44iskInfo\x12\r\n\x05\x62oard\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\r\n\x05label\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\t\x12\x14\n\x0cused_percent\x18\x05 \x01(\t\"\xe4\x01\n\x0bParamServer\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\nparam_type\x18\x02 \x01(\x0e\x32\x1a.service_manager.ParamType\x12\x13\n\tint_value\x18\x03 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x12\x14\n\nbool_value\x18\x05 \x01(\x08H\x00\x12\x16\n\x0cstring_value\x18\n \x01(\tH\x00\x12.\n\tdisk_info\x18\x0b \x01(\x0b\x32\x19.service_manager.DiskInfoH\x00\x42\r\n\x0bparam_value\"E\n\x0fParamServerList\x12\x32\n\x0cparam_server\x18\x01 \x03(\x0b\x32\x1c.service_manager.ParamServer\"+\n\nLogContext\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontext\x18\x02 \x01(\t*\x91\x01\n\x11NodeGroupCategory\x12\x08\n\x04NONE\x10\x00\x12\r\n\tALL_NODES\x10\x01\x12\x0e\n\nCORE_NODES\x10\x02\x12\x12\n\x0eOPTIONAL_NODES\x10\x03\x12\x18\n\x14MANUAL_STARTED_NODES\x10\x04\x12\x16\n\x12\x41UTO_STARTED_NODES\x10\x05\x12\r\n\tCMD_NODES\x10\x06*A\n\nOrinStatus\x12\x10\n\x0c\x42OARD_UNKOWN\x10\x00\x12\x0e\n\nBOARD_DEAD\x10\x01\x12\x11\n\rBOARD_RUNNING\x10\x02*M\n\nNodeStatus\x12\n\n\x06UNKOWN\x10\x00\x12\x08\n\x04\x44\x45\x41\x44\x10\x01\x12\x0c\n\x08STARTING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\x0e\n\nRESTARTING\x10\x04*R\n\tParamType\x12\x0b\n\x07NOT_SET\x10\x00\x12\x07\n\x03INT\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\x12\n\n\x06STRING\x10\n\x12\r\n\tDISK_INFO\x10\x0b\x32\xcd\x05\n\x0fLauncherService\x12\x44\n\x07Restart\x12\x1f.service_manager.NodeCollection\x1a\x16.google.protobuf.Empty\"\x00\x12\x42\n\x05Start\x12\x1f.service_manager.NodeCollection\x1a\x16.google.protobuf.Empty\"\x00\x12\x41\n\x04Stop\x12\x1f.service_manager.NodeCollection\x1a\x16.google.protobuf.Empty\"\x00\x12R\n\x06Status\x12\x1f.service_manager.NodeCollection\x1a%.service_manager.NodeStatusCollection\"\x00\x12<\n\x03Log\x12\x1b.service_manager.LogContext\x1a\x16.google.protobuf.Empty\"\x00\x12<\n\x07Options\x12\x17.service_manager.Option\x1a\x16.google.protobuf.Empty\"\x00\x12\x46\n\nOrinStatus\x12\x16.google.protobuf.Empty\x1a\x1e.service_manager.OneOrinStatus\"\x00\x12\x42\n\x08SetParam\x12\x1c.service_manager.ParamServer\x1a\x16.google.protobuf.Empty\"\x00\x12H\n\x08GetParam\x12\x1c.service_manager.ParamServer\x1a\x1c.service_manager.ParamServer\"\x00\x12G\n\tListParam\x12\x16.google.protobuf.Empty\x1a .service_manager.ParamServerList\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_NODEGROUPCATEGORY = _descriptor.EnumDescriptor(
  name='NodeGroupCategory',
  full_name='service_manager.NodeGroupCategory',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALL_NODES', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CORE_NODES', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OPTIONAL_NODES', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MANUAL_STARTED_NODES', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUTO_STARTED_NODES', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CMD_NODES', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1010,
  serialized_end=1155,
)
_sym_db.RegisterEnumDescriptor(_NODEGROUPCATEGORY)

NodeGroupCategory = enum_type_wrapper.EnumTypeWrapper(_NODEGROUPCATEGORY)
_ORINSTATUS = _descriptor.EnumDescriptor(
  name='OrinStatus',
  full_name='service_manager.OrinStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOARD_UNKOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOARD_DEAD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOARD_RUNNING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1157,
  serialized_end=1222,
)
_sym_db.RegisterEnumDescriptor(_ORINSTATUS)

OrinStatus = enum_type_wrapper.EnumTypeWrapper(_ORINSTATUS)
_NODESTATUS = _descriptor.EnumDescriptor(
  name='NodeStatus',
  full_name='service_manager.NodeStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEAD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STARTING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESTARTING', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1224,
  serialized_end=1301,
)
_sym_db.RegisterEnumDescriptor(_NODESTATUS)

NodeStatus = enum_type_wrapper.EnumTypeWrapper(_NODESTATUS)
_PARAMTYPE = _descriptor.EnumDescriptor(
  name='ParamType',
  full_name='service_manager.ParamType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_SET', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=4, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISK_INFO', index=5, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1303,
  serialized_end=1385,
)
_sym_db.RegisterEnumDescriptor(_PARAMTYPE)

ParamType = enum_type_wrapper.EnumTypeWrapper(_PARAMTYPE)
NONE = 0
ALL_NODES = 1
CORE_NODES = 2
OPTIONAL_NODES = 3
MANUAL_STARTED_NODES = 4
AUTO_STARTED_NODES = 5
CMD_NODES = 6
BOARD_UNKOWN = 0
BOARD_DEAD = 1
BOARD_RUNNING = 2
UNKOWN = 0
DEAD = 1
STARTING = 2
RUNNING = 3
RESTARTING = 4
NOT_SET = 0
INT = 1
DOUBLE = 2
BOOL = 3
STRING = 10
DISK_INFO = 11



_ONENODESTATUS = _descriptor.Descriptor(
  name='OneNodeStatus',
  full_name='service_manager.OneNodeStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='service_manager.OneNodeStatus.node', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='service_manager.OneNodeStatus.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pid', full_name='service_manager.OneNodeStatus.pid', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cmd', full_name='service_manager.OneNodeStatus.cmd', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='log', full_name='service_manager.OneNodeStatus.log', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group', full_name='service_manager.OneNodeStatus.group', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=88,
  serialized_end=216,
)


_NODESTATUSCOLLECTION = _descriptor.Descriptor(
  name='NodeStatusCollection',
  full_name='service_manager.NodeStatusCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_status', full_name='service_manager.NodeStatusCollection.node_status', index=0,
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
  serialized_start=218,
  serialized_end=293,
)


_NODECOLLECTION = _descriptor.Descriptor(
  name='NodeCollection',
  full_name='service_manager.NodeCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='service_manager.NodeCollection.nodes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='node_group', full_name='service_manager.NodeCollection.node_group', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sim_status', full_name='service_manager.NodeCollection.sim_status', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args', full_name='service_manager.NodeCollection.args', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identity', full_name='service_manager.NodeCollection.identity', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=296,
  serialized_end=435,
)


_LOGMESSAGE = _descriptor.Descriptor(
  name='LogMessage',
  full_name='service_manager.LogMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='service_manager.LogMessage.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=437,
  serialized_end=466,
)


_OPTION = _descriptor.Descriptor(
  name='Option',
  full_name='service_manager.Option',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gflags', full_name='service_manager.Option.gflags', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=468,
  serialized_end=492,
)


_ONEORINSTATUS = _descriptor.Descriptor(
  name='OneOrinStatus',
  full_name='service_manager.OneOrinStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='service_manager.OneOrinStatus.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='service_manager.OneOrinStatus.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=494,
  serialized_end=568,
)


_DISKINFO = _descriptor.Descriptor(
  name='DiskInfo',
  full_name='service_manager.DiskInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='board', full_name='service_manager.DiskInfo.board', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='service_manager.DiskInfo.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='service_manager.DiskInfo.label', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='service_manager.DiskInfo.size', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='used_percent', full_name='service_manager.DiskInfo.used_percent', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=570,
  serialized_end=660,
)


_PARAMSERVER = _descriptor.Descriptor(
  name='ParamServer',
  full_name='service_manager.ParamServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='service_manager.ParamServer.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='param_type', full_name='service_manager.ParamServer.param_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='service_manager.ParamServer.int_value', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='service_manager.ParamServer.double_value', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='service_manager.ParamServer.bool_value', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='service_manager.ParamServer.string_value', index=5,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disk_info', full_name='service_manager.ParamServer.disk_info', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='param_value', full_name='service_manager.ParamServer.param_value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=663,
  serialized_end=891,
)


_PARAMSERVERLIST = _descriptor.Descriptor(
  name='ParamServerList',
  full_name='service_manager.ParamServerList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_server', full_name='service_manager.ParamServerList.param_server', index=0,
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
  serialized_start=893,
  serialized_end=962,
)


_LOGCONTEXT = _descriptor.Descriptor(
  name='LogContext',
  full_name='service_manager.LogContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='service_manager.LogContext.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='context', full_name='service_manager.LogContext.context', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=964,
  serialized_end=1007,
)

_ONENODESTATUS.fields_by_name['status'].enum_type = _NODESTATUS
_NODESTATUSCOLLECTION.fields_by_name['node_status'].message_type = _ONENODESTATUS
_NODECOLLECTION.fields_by_name['node_group'].enum_type = _NODEGROUPCATEGORY
_ONEORINSTATUS.fields_by_name['status'].enum_type = _ORINSTATUS
_PARAMSERVER.fields_by_name['param_type'].enum_type = _PARAMTYPE
_PARAMSERVER.fields_by_name['disk_info'].message_type = _DISKINFO
_PARAMSERVER.oneofs_by_name['param_value'].fields.append(
  _PARAMSERVER.fields_by_name['int_value'])
_PARAMSERVER.fields_by_name['int_value'].containing_oneof = _PARAMSERVER.oneofs_by_name['param_value']
_PARAMSERVER.oneofs_by_name['param_value'].fields.append(
  _PARAMSERVER.fields_by_name['double_value'])
_PARAMSERVER.fields_by_name['double_value'].containing_oneof = _PARAMSERVER.oneofs_by_name['param_value']
_PARAMSERVER.oneofs_by_name['param_value'].fields.append(
  _PARAMSERVER.fields_by_name['bool_value'])
_PARAMSERVER.fields_by_name['bool_value'].containing_oneof = _PARAMSERVER.oneofs_by_name['param_value']
_PARAMSERVER.oneofs_by_name['param_value'].fields.append(
  _PARAMSERVER.fields_by_name['string_value'])
_PARAMSERVER.fields_by_name['string_value'].containing_oneof = _PARAMSERVER.oneofs_by_name['param_value']
_PARAMSERVER.oneofs_by_name['param_value'].fields.append(
  _PARAMSERVER.fields_by_name['disk_info'])
_PARAMSERVER.fields_by_name['disk_info'].containing_oneof = _PARAMSERVER.oneofs_by_name['param_value']
_PARAMSERVERLIST.fields_by_name['param_server'].message_type = _PARAMSERVER
DESCRIPTOR.message_types_by_name['OneNodeStatus'] = _ONENODESTATUS
DESCRIPTOR.message_types_by_name['NodeStatusCollection'] = _NODESTATUSCOLLECTION
DESCRIPTOR.message_types_by_name['NodeCollection'] = _NODECOLLECTION
DESCRIPTOR.message_types_by_name['LogMessage'] = _LOGMESSAGE
DESCRIPTOR.message_types_by_name['Option'] = _OPTION
DESCRIPTOR.message_types_by_name['OneOrinStatus'] = _ONEORINSTATUS
DESCRIPTOR.message_types_by_name['DiskInfo'] = _DISKINFO
DESCRIPTOR.message_types_by_name['ParamServer'] = _PARAMSERVER
DESCRIPTOR.message_types_by_name['ParamServerList'] = _PARAMSERVERLIST
DESCRIPTOR.message_types_by_name['LogContext'] = _LOGCONTEXT
DESCRIPTOR.enum_types_by_name['NodeGroupCategory'] = _NODEGROUPCATEGORY
DESCRIPTOR.enum_types_by_name['OrinStatus'] = _ORINSTATUS
DESCRIPTOR.enum_types_by_name['NodeStatus'] = _NODESTATUS
DESCRIPTOR.enum_types_by_name['ParamType'] = _PARAMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OneNodeStatus = _reflection.GeneratedProtocolMessageType('OneNodeStatus', (_message.Message,), {
  'DESCRIPTOR' : _ONENODESTATUS,
  '__module__' : 'service_protos.launcher_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.OneNodeStatus)
  })
_sym_db.RegisterMessage(OneNodeStatus)

NodeStatusCollection = _reflection.GeneratedProtocolMessageType('NodeStatusCollection', (_message.Message,), {
  'DESCRIPTOR' : _NODESTATUSCOLLECTION,
  '__module__' : 'service_protos.launcher_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.NodeStatusCollection)
  })
_sym_db.RegisterMessage(NodeStatusCollection)

NodeCollection = _reflection.GeneratedProtocolMessageType('NodeCollection', (_message.Message,), {
  'DESCRIPTOR' : _NODECOLLECTION,
  '__module__' : 'service_protos.launcher_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.NodeCollection)
  })
_sym_db.RegisterMessage(NodeCollection)

LogMessage = _reflection.GeneratedProtocolMessageType('LogMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOGMESSAGE,
  '__module__' : 'service_protos.launcher_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.LogMessage)
  })
_sym_db.RegisterMessage(LogMessage)

Option = _reflection.GeneratedProtocolMessageType('Option', (_message.Message,), {
  'DESCRIPTOR' : _OPTION,
  '__module__' : 'service_protos.launcher_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.Option)
  })
_sym_db.RegisterMessage(Option)

OneOrinStatus = _reflection.GeneratedProtocolMessageType('OneOrinStatus', (_message.Message,), {
  'DESCRIPTOR' : _ONEORINSTATUS,
  '__module__' : 'service_protos.launcher_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.OneOrinStatus)
  })
_sym_db.RegisterMessage(OneOrinStatus)

DiskInfo = _reflection.GeneratedProtocolMessageType('DiskInfo', (_message.Message,), {
  'DESCRIPTOR' : _DISKINFO,
  '__module__' : 'service_protos.launcher_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.DiskInfo)
  })
_sym_db.RegisterMessage(DiskInfo)

ParamServer = _reflection.GeneratedProtocolMessageType('ParamServer', (_message.Message,), {
  'DESCRIPTOR' : _PARAMSERVER,
  '__module__' : 'service_protos.launcher_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.ParamServer)
  })
_sym_db.RegisterMessage(ParamServer)

ParamServerList = _reflection.GeneratedProtocolMessageType('ParamServerList', (_message.Message,), {
  'DESCRIPTOR' : _PARAMSERVERLIST,
  '__module__' : 'service_protos.launcher_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.ParamServerList)
  })
_sym_db.RegisterMessage(ParamServerList)

LogContext = _reflection.GeneratedProtocolMessageType('LogContext', (_message.Message,), {
  'DESCRIPTOR' : _LOGCONTEXT,
  '__module__' : 'service_protos.launcher_service_pb2'
  # @@protoc_insertion_point(class_scope:service_manager.LogContext)
  })
_sym_db.RegisterMessage(LogContext)



_LAUNCHERSERVICE = _descriptor.ServiceDescriptor(
  name='LauncherService',
  full_name='service_manager.LauncherService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1388,
  serialized_end=2105,
  methods=[
  _descriptor.MethodDescriptor(
    name='Restart',
    full_name='service_manager.LauncherService.Restart',
    index=0,
    containing_service=None,
    input_type=_NODECOLLECTION,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Start',
    full_name='service_manager.LauncherService.Start',
    index=1,
    containing_service=None,
    input_type=_NODECOLLECTION,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Stop',
    full_name='service_manager.LauncherService.Stop',
    index=2,
    containing_service=None,
    input_type=_NODECOLLECTION,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Status',
    full_name='service_manager.LauncherService.Status',
    index=3,
    containing_service=None,
    input_type=_NODECOLLECTION,
    output_type=_NODESTATUSCOLLECTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Log',
    full_name='service_manager.LauncherService.Log',
    index=4,
    containing_service=None,
    input_type=_LOGCONTEXT,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Options',
    full_name='service_manager.LauncherService.Options',
    index=5,
    containing_service=None,
    input_type=_OPTION,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='OrinStatus',
    full_name='service_manager.LauncherService.OrinStatus',
    index=6,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_ONEORINSTATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetParam',
    full_name='service_manager.LauncherService.SetParam',
    index=7,
    containing_service=None,
    input_type=_PARAMSERVER,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetParam',
    full_name='service_manager.LauncherService.GetParam',
    index=8,
    containing_service=None,
    input_type=_PARAMSERVER,
    output_type=_PARAMSERVER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListParam',
    full_name='service_manager.LauncherService.ListParam',
    index=9,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_PARAMSERVERLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LAUNCHERSERVICE)

DESCRIPTOR.services_by_name['LauncherService'] = _LAUNCHERSERVICE

# @@protoc_insertion_point(module_scope)