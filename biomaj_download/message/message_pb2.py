# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

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
  name='message.proto',
  package='biomaj',
  serialized_pb=_b('\n\rmessage.proto\x12\x06\x62iomaj\"\x94\x02\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04root\x18\x02 \x01(\t\x12\x0f\n\x07save_as\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\'\n\x08metadata\x18\x05 \x01(\x0b\x32\x15.biomaj.File.MetaData\x1a\xa8\x01\n\x08MetaData\x12\x13\n\x0bpermissions\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x03\x12\x0c\n\x04hash\x18\x04 \x01(\t\x12\x0c\n\x04year\x18\x05 \x01(\x05\x12\r\n\x05month\x18\x06 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x07 \x01(\x05\x12\x0e\n\x06\x66ormat\x18\x08 \x01(\t\x12\x0b\n\x03md5\x18\t \x01(\t\x12\x15\n\rdownload_time\x18\n \x01(\x03\"\'\n\x08\x46ileList\x12\x1b\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x0c.biomaj.File\"\x86\x02\n\tOperation\x12)\n\x04type\x18\x01 \x02(\x0e\x32\x1b.biomaj.Operation.OPERATION\x12&\n\x08\x64ownload\x18\x02 \x01(\x0b\x32\x14.biomaj.DownloadFile\x12 \n\x07process\x18\x03 \x01(\x0b\x32\x0f.biomaj.Process\x12&\n\x05trace\x18\x04 \x01(\x0b\x32\x17.biomaj.Operation.Trace\x1a*\n\x05Trace\x12\x10\n\x08trace_id\x18\x01 \x02(\t\x12\x0f\n\x07span_id\x18\x02 \x02(\t\"0\n\tOPERATION\x12\x08\n\x04LIST\x10\x00\x12\x0c\n\x08\x44OWNLOAD\x10\x01\x12\x0b\n\x07PROCESS\x10\x02\"\x17\n\x07Process\x12\x0c\n\x04\x65xec\x18\x01 \x02(\t\"\xcc\t\n\x0c\x44ownloadFile\x12\x0c\n\x04\x62\x61nk\x18\x01 \x02(\t\x12\x0f\n\x07session\x18\x02 \x02(\t\x12\x11\n\tlocal_dir\x18\x03 \x02(\t\x12\x18\n\x10timeout_download\x18\x04 \x01(\x05\x12\x34\n\x0bremote_file\x18\x05 \x02(\x0b\x32\x1f.biomaj.DownloadFile.RemoteFile\x12)\n\x05proxy\x18\x06 \x01(\x0b\x32\x1a.biomaj.DownloadFile.Proxy\x12:\n\x0bhttp_method\x18\x08 \x01(\x0e\x32 .biomaj.DownloadFile.HTTP_METHOD:\x03GET\x1a$\n\x05Param\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\x1a\xcd\x03\n\tHttpParse\x12\x91\x01\n\x08\x64ir_line\x18\x01 \x02(\t:\x7f<img[\\s]+src=\"[\\S]+\"[\\s]+alt=\"\\[DIR\\]\"[\\s]*/?>[\\s]*<a[\\s]+href=\"([\\S]+)/\"[\\s]*>.*([\\d]{2}-[\\w\\d]{2,5}-[\\d]{4}\\s[\\d]{2}:[\\d]{2})\x12\xa5\x01\n\tfile_line\x18\x02 \x02(\t:\x91\x01<img[\\s]+src=\"[\\S]+\"[\\s]+alt=\"\\[[\\s]+\\]\"[\\s]*/?>[\\s]<a[\\s]+href=\"([\\S]+)\".*([\\d]{2}-[\\w\\d]{2,5}-[\\d]{4}\\s[\\d]{2}:[\\d]{2})[\\s]+([\\d\\.]+[MKG]{0,1})\x12\x13\n\x08\x64ir_name\x18\x03 \x02(\x05:\x01\x31\x12\x13\n\x08\x64ir_date\x18\x04 \x02(\x05:\x01\x32\x12\x14\n\tfile_name\x18\x05 \x02(\x05:\x01\x31\x12\x14\n\tfile_date\x18\x06 \x02(\x05:\x01\x32\x12\x18\n\x10\x66ile_date_format\x18\x07 \x01(\t\x12\x14\n\tfile_size\x18\x08 \x02(\x05:\x01\x33\x1a\x94\x02\n\nRemoteFile\x12\x1b\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x0c.biomaj.File\x12/\n\x08protocol\x18\x02 \x02(\x0e\x32\x1d.biomaj.DownloadFile.Protocol\x12\x0e\n\x06server\x18\x03 \x02(\t\x12\x12\n\nremote_dir\x18\x04 \x02(\t\x12\x0f\n\x07save_as\x18\x05 \x01(\t\x12)\n\x05param\x18\x06 \x03(\x0b\x32\x1a.biomaj.DownloadFile.Param\x12\x32\n\nhttp_parse\x18\x07 \x01(\x0b\x32\x1e.biomaj.DownloadFile.HttpParse\x12\x13\n\x0b\x63redentials\x18\x08 \x01(\t\x12\x0f\n\x07matches\x18\t \x03(\t\x1a*\n\x05Proxy\x12\r\n\x05proxy\x18\x01 \x02(\t\x12\x12\n\nproxy_auth\x18\x02 \x01(\t\"x\n\x08Protocol\x12\x07\n\x03\x46TP\x10\x00\x12\x08\n\x04SFTP\x10\x01\x12\x08\n\x04HTTP\x10\x02\x12\t\n\x05HTTPS\x10\x03\x12\r\n\tDIRECTFTP\x10\x04\x12\x0e\n\nDIRECTHTTP\x10\x05\x12\x0f\n\x0b\x44IRECTHTTPS\x10\x06\x12\t\n\x05LOCAL\x10\x07\x12\t\n\x05RSYNC\x10\x08\" \n\x0bHTTP_METHOD\x12\x07\n\x03GET\x10\x00\x12\x08\n\x04POST\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_OPERATION_OPERATION = _descriptor.EnumDescriptor(
  name='OPERATION',
  full_name='biomaj.Operation.OPERATION',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LIST', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROCESS', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=560,
  serialized_end=608,
)
_sym_db.RegisterEnumDescriptor(_OPERATION_OPERATION)

_DOWNLOADFILE_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='biomaj.DownloadFile.Protocol',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FTP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SFTP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTTP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTTPS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECTFTP', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECTHTTP', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DIRECTHTTPS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RSYNC', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1710,
  serialized_end=1830,
)
_sym_db.RegisterEnumDescriptor(_DOWNLOADFILE_PROTOCOL)

_DOWNLOADFILE_HTTP_METHOD = _descriptor.EnumDescriptor(
  name='HTTP_METHOD',
  full_name='biomaj.DownloadFile.HTTP_METHOD',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1832,
  serialized_end=1864,
)
_sym_db.RegisterEnumDescriptor(_DOWNLOADFILE_HTTP_METHOD)


_FILE_METADATA = _descriptor.Descriptor(
  name='MetaData',
  full_name='biomaj.File.MetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='permissions', full_name='biomaj.File.MetaData.permissions', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='biomaj.File.MetaData.group', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='biomaj.File.MetaData.size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hash', full_name='biomaj.File.MetaData.hash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='year', full_name='biomaj.File.MetaData.year', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='month', full_name='biomaj.File.MetaData.month', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='day', full_name='biomaj.File.MetaData.day', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='format', full_name='biomaj.File.MetaData.format', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='md5', full_name='biomaj.File.MetaData.md5', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='download_time', full_name='biomaj.File.MetaData.download_time', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=302,
)

_FILE = _descriptor.Descriptor(
  name='File',
  full_name='biomaj.File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='biomaj.File.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='root', full_name='biomaj.File.root', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_as', full_name='biomaj.File.save_as', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='biomaj.File.url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='biomaj.File.metadata', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FILE_METADATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=302,
)


_FILELIST = _descriptor.Descriptor(
  name='FileList',
  full_name='biomaj.FileList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='files', full_name='biomaj.FileList.files', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=343,
)


_OPERATION_TRACE = _descriptor.Descriptor(
  name='Trace',
  full_name='biomaj.Operation.Trace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trace_id', full_name='biomaj.Operation.Trace.trace_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='span_id', full_name='biomaj.Operation.Trace.span_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=558,
)

_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='biomaj.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='biomaj.Operation.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='download', full_name='biomaj.Operation.download', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='process', full_name='biomaj.Operation.process', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trace', full_name='biomaj.Operation.trace', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_OPERATION_TRACE, ],
  enum_types=[
    _OPERATION_OPERATION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=608,
)


_PROCESS = _descriptor.Descriptor(
  name='Process',
  full_name='biomaj.Process',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exec', full_name='biomaj.Process.exec', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=633,
)


_DOWNLOADFILE_PARAM = _descriptor.Descriptor(
  name='Param',
  full_name='biomaj.DownloadFile.Param',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='biomaj.DownloadFile.Param.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='biomaj.DownloadFile.Param.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=885,
  serialized_end=921,
)

_DOWNLOADFILE_HTTPPARSE = _descriptor.Descriptor(
  name='HttpParse',
  full_name='biomaj.DownloadFile.HttpParse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dir_line', full_name='biomaj.DownloadFile.HttpParse.dir_line', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("<img[\\s]+src=\"[\\S]+\"[\\s]+alt=\"\\[DIR\\]\"[\\s]*/?>[\\s]*<a[\\s]+href=\"([\\S]+)/\"[\\s]*>.*([\\d]{2}-[\\w\\d]{2,5}-[\\d]{4}\\s[\\d]{2}:[\\d]{2})").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_line', full_name='biomaj.DownloadFile.HttpParse.file_line', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=_b("<img[\\s]+src=\"[\\S]+\"[\\s]+alt=\"\\[[\\s]+\\]\"[\\s]*/?>[\\s]<a[\\s]+href=\"([\\S]+)\".*([\\d]{2}-[\\w\\d]{2,5}-[\\d]{4}\\s[\\d]{2}:[\\d]{2})[\\s]+([\\d\\.]+[MKG]{0,1})").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dir_name', full_name='biomaj.DownloadFile.HttpParse.dir_name', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dir_date', full_name='biomaj.DownloadFile.HttpParse.dir_date', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='biomaj.DownloadFile.HttpParse.file_name', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_date', full_name='biomaj.DownloadFile.HttpParse.file_date', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_date_format', full_name='biomaj.DownloadFile.HttpParse.file_date_format', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='biomaj.DownloadFile.HttpParse.file_size', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=3,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=924,
  serialized_end=1385,
)

_DOWNLOADFILE_REMOTEFILE = _descriptor.Descriptor(
  name='RemoteFile',
  full_name='biomaj.DownloadFile.RemoteFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='files', full_name='biomaj.DownloadFile.RemoteFile.files', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='biomaj.DownloadFile.RemoteFile.protocol', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server', full_name='biomaj.DownloadFile.RemoteFile.server', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_dir', full_name='biomaj.DownloadFile.RemoteFile.remote_dir', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='save_as', full_name='biomaj.DownloadFile.RemoteFile.save_as', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param', full_name='biomaj.DownloadFile.RemoteFile.param', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='http_parse', full_name='biomaj.DownloadFile.RemoteFile.http_parse', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='credentials', full_name='biomaj.DownloadFile.RemoteFile.credentials', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='matches', full_name='biomaj.DownloadFile.RemoteFile.matches', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1388,
  serialized_end=1664,
)

_DOWNLOADFILE_PROXY = _descriptor.Descriptor(
  name='Proxy',
  full_name='biomaj.DownloadFile.Proxy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='proxy', full_name='biomaj.DownloadFile.Proxy.proxy', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proxy_auth', full_name='biomaj.DownloadFile.Proxy.proxy_auth', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1666,
  serialized_end=1708,
)

_DOWNLOADFILE = _descriptor.Descriptor(
  name='DownloadFile',
  full_name='biomaj.DownloadFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bank', full_name='biomaj.DownloadFile.bank', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='biomaj.DownloadFile.session', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_dir', full_name='biomaj.DownloadFile.local_dir', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeout_download', full_name='biomaj.DownloadFile.timeout_download', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remote_file', full_name='biomaj.DownloadFile.remote_file', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proxy', full_name='biomaj.DownloadFile.proxy', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='http_method', full_name='biomaj.DownloadFile.http_method', index=6,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DOWNLOADFILE_PARAM, _DOWNLOADFILE_HTTPPARSE, _DOWNLOADFILE_REMOTEFILE, _DOWNLOADFILE_PROXY, ],
  enum_types=[
    _DOWNLOADFILE_PROTOCOL,
    _DOWNLOADFILE_HTTP_METHOD,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=636,
  serialized_end=1864,
)

_FILE_METADATA.containing_type = _FILE
_FILE.fields_by_name['metadata'].message_type = _FILE_METADATA
_FILELIST.fields_by_name['files'].message_type = _FILE
_OPERATION_TRACE.containing_type = _OPERATION
_OPERATION.fields_by_name['type'].enum_type = _OPERATION_OPERATION
_OPERATION.fields_by_name['download'].message_type = _DOWNLOADFILE
_OPERATION.fields_by_name['process'].message_type = _PROCESS
_OPERATION.fields_by_name['trace'].message_type = _OPERATION_TRACE
_OPERATION_OPERATION.containing_type = _OPERATION
_DOWNLOADFILE_PARAM.containing_type = _DOWNLOADFILE
_DOWNLOADFILE_HTTPPARSE.containing_type = _DOWNLOADFILE
_DOWNLOADFILE_REMOTEFILE.fields_by_name['files'].message_type = _FILE
_DOWNLOADFILE_REMOTEFILE.fields_by_name['protocol'].enum_type = _DOWNLOADFILE_PROTOCOL
_DOWNLOADFILE_REMOTEFILE.fields_by_name['param'].message_type = _DOWNLOADFILE_PARAM
_DOWNLOADFILE_REMOTEFILE.fields_by_name['http_parse'].message_type = _DOWNLOADFILE_HTTPPARSE
_DOWNLOADFILE_REMOTEFILE.containing_type = _DOWNLOADFILE
_DOWNLOADFILE_PROXY.containing_type = _DOWNLOADFILE
_DOWNLOADFILE.fields_by_name['remote_file'].message_type = _DOWNLOADFILE_REMOTEFILE
_DOWNLOADFILE.fields_by_name['proxy'].message_type = _DOWNLOADFILE_PROXY
_DOWNLOADFILE.fields_by_name['http_method'].enum_type = _DOWNLOADFILE_HTTP_METHOD
_DOWNLOADFILE_PROTOCOL.containing_type = _DOWNLOADFILE
_DOWNLOADFILE_HTTP_METHOD.containing_type = _DOWNLOADFILE
DESCRIPTOR.message_types_by_name['File'] = _FILE
DESCRIPTOR.message_types_by_name['FileList'] = _FILELIST
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
DESCRIPTOR.message_types_by_name['Process'] = _PROCESS
DESCRIPTOR.message_types_by_name['DownloadFile'] = _DOWNLOADFILE

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), dict(

  MetaData = _reflection.GeneratedProtocolMessageType('MetaData', (_message.Message,), dict(
    DESCRIPTOR = _FILE_METADATA,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.File.MetaData)
    ))
  ,
  DESCRIPTOR = _FILE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:biomaj.File)
  ))
_sym_db.RegisterMessage(File)
_sym_db.RegisterMessage(File.MetaData)

FileList = _reflection.GeneratedProtocolMessageType('FileList', (_message.Message,), dict(
  DESCRIPTOR = _FILELIST,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:biomaj.FileList)
  ))
_sym_db.RegisterMessage(FileList)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(

  Trace = _reflection.GeneratedProtocolMessageType('Trace', (_message.Message,), dict(
    DESCRIPTOR = _OPERATION_TRACE,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.Operation.Trace)
    ))
  ,
  DESCRIPTOR = _OPERATION,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:biomaj.Operation)
  ))
_sym_db.RegisterMessage(Operation)
_sym_db.RegisterMessage(Operation.Trace)

Process = _reflection.GeneratedProtocolMessageType('Process', (_message.Message,), dict(
  DESCRIPTOR = _PROCESS,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:biomaj.Process)
  ))
_sym_db.RegisterMessage(Process)

DownloadFile = _reflection.GeneratedProtocolMessageType('DownloadFile', (_message.Message,), dict(

  Param = _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADFILE_PARAM,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.DownloadFile.Param)
    ))
  ,

  HttpParse = _reflection.GeneratedProtocolMessageType('HttpParse', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADFILE_HTTPPARSE,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.DownloadFile.HttpParse)
    ))
  ,

  RemoteFile = _reflection.GeneratedProtocolMessageType('RemoteFile', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADFILE_REMOTEFILE,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.DownloadFile.RemoteFile)
    ))
  ,

  Proxy = _reflection.GeneratedProtocolMessageType('Proxy', (_message.Message,), dict(
    DESCRIPTOR = _DOWNLOADFILE_PROXY,
    __module__ = 'message_pb2'
    # @@protoc_insertion_point(class_scope:biomaj.DownloadFile.Proxy)
    ))
  ,
  DESCRIPTOR = _DOWNLOADFILE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:biomaj.DownloadFile)
  ))
_sym_db.RegisterMessage(DownloadFile)
_sym_db.RegisterMessage(DownloadFile.Param)
_sym_db.RegisterMessage(DownloadFile.HttpParse)
_sym_db.RegisterMessage(DownloadFile.RemoteFile)
_sym_db.RegisterMessage(DownloadFile.Proxy)


# @@protoc_insertion_point(module_scope)
