# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/proxy/http/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/proxy/http/config.proto',
  package='v2ray.core.proxy.http',
  syntax='proto3',
  serialized_pb=_b('\n&v2ray.com/core/proxy/http/config.proto\x12\x15v2ray.core.proxy.http\"\xc8\x01\n\x0cServerConfig\x12\x13\n\x07timeout\x18\x01 \x01(\rB\x02\x18\x01\x12\x43\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32\x31.v2ray.core.proxy.http.ServerConfig.AccountsEntry\x12\x19\n\x11\x61llow_transparent\x18\x03 \x01(\x08\x12\x12\n\nuser_level\x18\x04 \x01(\r\x1a/\n\rAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x0e\n\x0c\x43lientConfigB;\n\x19\x63om.v2ray.core.proxy.httpP\x01Z\x04http\xaa\x02\x15V2Ray.Core.Proxy.Httpb\x06proto3')
)




_SERVERCONFIG_ACCOUNTSENTRY = _descriptor.Descriptor(
  name='AccountsEntry',
  full_name='v2ray.core.proxy.http.ServerConfig.AccountsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v2ray.core.proxy.http.ServerConfig.AccountsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v2ray.core.proxy.http.ServerConfig.AccountsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=266,
)

_SERVERCONFIG = _descriptor.Descriptor(
  name='ServerConfig',
  full_name='v2ray.core.proxy.http.ServerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout', full_name='v2ray.core.proxy.http.ServerConfig.timeout', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accounts', full_name='v2ray.core.proxy.http.ServerConfig.accounts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow_transparent', full_name='v2ray.core.proxy.http.ServerConfig.allow_transparent', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_level', full_name='v2ray.core.proxy.http.ServerConfig.user_level', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SERVERCONFIG_ACCOUNTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=266,
)


_CLIENTCONFIG = _descriptor.Descriptor(
  name='ClientConfig',
  full_name='v2ray.core.proxy.http.ClientConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=282,
)

_SERVERCONFIG_ACCOUNTSENTRY.containing_type = _SERVERCONFIG
_SERVERCONFIG.fields_by_name['accounts'].message_type = _SERVERCONFIG_ACCOUNTSENTRY
DESCRIPTOR.message_types_by_name['ServerConfig'] = _SERVERCONFIG
DESCRIPTOR.message_types_by_name['ClientConfig'] = _CLIENTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerConfig = _reflection.GeneratedProtocolMessageType('ServerConfig', (_message.Message,), dict(

  AccountsEntry = _reflection.GeneratedProtocolMessageType('AccountsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SERVERCONFIG_ACCOUNTSENTRY,
    __module__ = 'v2ray.com.core.proxy.http.config_pb2'
    # @@protoc_insertion_point(class_scope:v2ray.core.proxy.http.ServerConfig.AccountsEntry)
    ))
  ,
  DESCRIPTOR = _SERVERCONFIG,
  __module__ = 'v2ray.com.core.proxy.http.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.http.ServerConfig)
  ))
_sym_db.RegisterMessage(ServerConfig)
_sym_db.RegisterMessage(ServerConfig.AccountsEntry)

ClientConfig = _reflection.GeneratedProtocolMessageType('ClientConfig', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTCONFIG,
  __module__ = 'v2ray.com.core.proxy.http.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.http.ClientConfig)
  ))
_sym_db.RegisterMessage(ClientConfig)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\031com.v2ray.core.proxy.httpP\001Z\004http\252\002\025V2Ray.Core.Proxy.Http'))
_SERVERCONFIG_ACCOUNTSENTRY.has_options = True
_SERVERCONFIG_ACCOUNTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SERVERCONFIG.fields_by_name['timeout'].has_options = True
_SERVERCONFIG.fields_by_name['timeout']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)