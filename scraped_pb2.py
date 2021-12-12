# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scraped.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='scraped.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rscraped.proto\"\xa9\x02\n\x07Scraped\x12\x0b\n\x03md5\x18\x01 \x01(\t\x12\x0c\n\x04sha1\x18\x02 \x01(\t\x12\x0e\n\x06sha256\x18\x03 \x01(\t\x12\x0e\n\x06sha512\x18\x04 \x01(\t\x12\x0c\n\x04mime\x18\x05 \x01(\t\x12\r\n\x05magic\x18\x06 \x01(\t\x12\x0f\n\x07strings\x18\x07 \x03(\t\x12\x10\n\x08\x66iletype\x18\x08 \x01(\t\x12\x16\n\x06macros\x18\t \x03(\x0b\x32\x06.Macro\x12\x1e\n\nindicators\x18\n \x03(\x0b\x32\n.Indicator\x12\x18\n\texecution\x18\x0b \x03(\x0b\x32\x05.Step\x12\x1f\n\x10\x66urther_analysis\x18\x0c \x03(\x0b\x32\x05.Step\x12\x0e\n\x06olevba\x18\r \x01(\t\x12\x0f\n\x07oledump\x18\x0e \x01(\t\x12\x0f\n\x07vmonkey\x18\x0f \x01(\t\"\x15\n\x05Macro\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"@\n\tIndicator\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08keywords\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"\x1b\n\x04Step\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\tb\x06proto3')
)




_SCRAPED = _descriptor.Descriptor(
  name='Scraped',
  full_name='Scraped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='md5', full_name='Scraped.md5', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sha1', full_name='Scraped.sha1', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sha256', full_name='Scraped.sha256', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sha512', full_name='Scraped.sha512', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mime', full_name='Scraped.mime', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='magic', full_name='Scraped.magic', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strings', full_name='Scraped.strings', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filetype', full_name='Scraped.filetype', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='macros', full_name='Scraped.macros', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indicators', full_name='Scraped.indicators', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execution', full_name='Scraped.execution', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='further_analysis', full_name='Scraped.further_analysis', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='olevba', full_name='Scraped.olevba', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oledump', full_name='Scraped.oledump', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vmonkey', full_name='Scraped.vmonkey', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=18,
  serialized_end=315,
)


_MACRO = _descriptor.Descriptor(
  name='Macro',
  full_name='Macro',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='Macro.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=317,
  serialized_end=338,
)


_INDICATOR = _descriptor.Descriptor(
  name='Indicator',
  full_name='Indicator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Indicator.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keywords', full_name='Indicator.keywords', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Indicator.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=340,
  serialized_end=404,
)


_STEP = _descriptor.Descriptor(
  name='Step',
  full_name='Step',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='Step.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=406,
  serialized_end=433,
)

_SCRAPED.fields_by_name['macros'].message_type = _MACRO
_SCRAPED.fields_by_name['indicators'].message_type = _INDICATOR
_SCRAPED.fields_by_name['execution'].message_type = _STEP
_SCRAPED.fields_by_name['further_analysis'].message_type = _STEP
DESCRIPTOR.message_types_by_name['Scraped'] = _SCRAPED
DESCRIPTOR.message_types_by_name['Macro'] = _MACRO
DESCRIPTOR.message_types_by_name['Indicator'] = _INDICATOR
DESCRIPTOR.message_types_by_name['Step'] = _STEP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Scraped = _reflection.GeneratedProtocolMessageType('Scraped', (_message.Message,), dict(
  DESCRIPTOR = _SCRAPED,
  __module__ = 'scraped_pb2'
  # @@protoc_insertion_point(class_scope:Scraped)
  ))
_sym_db.RegisterMessage(Scraped)

Macro = _reflection.GeneratedProtocolMessageType('Macro', (_message.Message,), dict(
  DESCRIPTOR = _MACRO,
  __module__ = 'scraped_pb2'
  # @@protoc_insertion_point(class_scope:Macro)
  ))
_sym_db.RegisterMessage(Macro)

Indicator = _reflection.GeneratedProtocolMessageType('Indicator', (_message.Message,), dict(
  DESCRIPTOR = _INDICATOR,
  __module__ = 'scraped_pb2'
  # @@protoc_insertion_point(class_scope:Indicator)
  ))
_sym_db.RegisterMessage(Indicator)

Step = _reflection.GeneratedProtocolMessageType('Step', (_message.Message,), dict(
  DESCRIPTOR = _STEP,
  __module__ = 'scraped_pb2'
  # @@protoc_insertion_point(class_scope:Step)
  ))
_sym_db.RegisterMessage(Step)


# @@protoc_insertion_point(module_scope)
