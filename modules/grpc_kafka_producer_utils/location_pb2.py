# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0elocation.proto\"w\n\x0fLocationMessage\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x1a\n\rcreation_time\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\x10\n\x0e_creation_time2?\n\x0fLocationService\x12,\n\x06\x43reate\x12\x10.LocationMessage\x1a\x10.LocationMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'location_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LOCATIONMESSAGE']._serialized_start=18
  _globals['_LOCATIONMESSAGE']._serialized_end=137
  _globals['_LOCATIONSERVICE']._serialized_start=139
  _globals['_LOCATIONSERVICE']._serialized_end=202
# @@protoc_insertion_point(module_scope)
