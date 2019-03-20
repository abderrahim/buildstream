# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buildstream/v2/artifact.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buildstream._protos.build.bazel.remote.execution.v2 import remote_execution_pb2 as build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2
from buildstream._protos.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='buildstream/v2/artifact.proto',
  package='buildstream.v2',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1d\x62uildstream/v2/artifact.proto\x12\x0e\x62uildstream.v2\x1a\x36\x62uild/bazel/remote/execution/v2/remote_execution.proto\x1a\x1cgoogle/api/annotations.proto\"\xde\x04\n\x08\x41rtifact\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x15\n\rbuild_success\x18\x02 \x01(\x08\x12\x13\n\x0b\x62uild_error\x18\x03 \x01(\t\x12\x1b\n\x13\x62uild_error_details\x18\x04 \x01(\t\x12\x12\n\nstrong_key\x18\x05 \x01(\t\x12\x10\n\x08weak_key\x18\x06 \x01(\t\x12\x16\n\x0ewas_workspaced\x18\x07 \x01(\x08\x12\x36\n\x05\x66iles\x18\x08 \x01(\x0b\x32\'.build.bazel.remote.execution.v2.Digest\x12\x37\n\nbuild_deps\x18\t \x03(\x0b\x32#.buildstream.v2.Artifact.Dependency\x12<\n\x0bpublic_data\x18\n \x01(\x0b\x32\'.build.bazel.remote.execution.v2.Digest\x12.\n\x04logs\x18\x0b \x03(\x0b\x32 .buildstream.v2.Artifact.LogFile\x12:\n\tbuildtree\x18\x0c \x01(\x0b\x32\'.build.bazel.remote.execution.v2.Digest\x1aM\n\nDependency\x12\x14\n\x0c\x65lement_name\x18\x01 \x01(\t\x12\x11\n\tcache_key\x18\x02 \x01(\t\x12\x16\n\x0ewas_workspaced\x18\x03 \x01(\x08\x1aP\n\x07LogFile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x37\n\x06\x64igest\x18\x02 \x01(\x0b\x32\'.build.bazel.remote.execution.v2.Digest\">\n\x12GetArtifactRequest\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x11\n\tcache_key\x18\x02 \x01(\t\"m\n\x15UpdateArtifactRequest\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x11\n\tcache_key\x18\x02 \x01(\t\x12*\n\x08\x61rtifact\x18\x03 \x01(\x0b\x32\x18.buildstream.v2.Artifact2\xb5\x01\n\x0f\x41rtifactService\x12M\n\x0bGetArtifact\x12\".buildstream.v2.GetArtifactRequest\x1a\x18.buildstream.v2.Artifact\"\x00\x12S\n\x0eUpdateArtifact\x12%.buildstream.v2.UpdateArtifactRequest\x1a\x18.buildstream.v2.Artifact\"\x00\x62\x06proto3')
  ,
  dependencies=[build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ARTIFACT_DEPENDENCY = _descriptor.Descriptor(
  name='Dependency',
  full_name='buildstream.v2.Artifact.Dependency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='element_name', full_name='buildstream.v2.Artifact.Dependency.element_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cache_key', full_name='buildstream.v2.Artifact.Dependency.cache_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='was_workspaced', full_name='buildstream.v2.Artifact.Dependency.was_workspaced', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=583,
  serialized_end=660,
)

_ARTIFACT_LOGFILE = _descriptor.Descriptor(
  name='LogFile',
  full_name='buildstream.v2.Artifact.LogFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='buildstream.v2.Artifact.LogFile.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='digest', full_name='buildstream.v2.Artifact.LogFile.digest', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=662,
  serialized_end=742,
)

_ARTIFACT = _descriptor.Descriptor(
  name='Artifact',
  full_name='buildstream.v2.Artifact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='buildstream.v2.Artifact.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_success', full_name='buildstream.v2.Artifact.build_success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_error', full_name='buildstream.v2.Artifact.build_error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_error_details', full_name='buildstream.v2.Artifact.build_error_details', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strong_key', full_name='buildstream.v2.Artifact.strong_key', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weak_key', full_name='buildstream.v2.Artifact.weak_key', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='was_workspaced', full_name='buildstream.v2.Artifact.was_workspaced', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='files', full_name='buildstream.v2.Artifact.files', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_deps', full_name='buildstream.v2.Artifact.build_deps', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_data', full_name='buildstream.v2.Artifact.public_data', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logs', full_name='buildstream.v2.Artifact.logs', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buildtree', full_name='buildstream.v2.Artifact.buildtree', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ARTIFACT_DEPENDENCY, _ARTIFACT_LOGFILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=742,
)


_GETARTIFACTREQUEST = _descriptor.Descriptor(
  name='GetArtifactRequest',
  full_name='buildstream.v2.GetArtifactRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='buildstream.v2.GetArtifactRequest.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cache_key', full_name='buildstream.v2.GetArtifactRequest.cache_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=744,
  serialized_end=806,
)


_UPDATEARTIFACTREQUEST = _descriptor.Descriptor(
  name='UpdateArtifactRequest',
  full_name='buildstream.v2.UpdateArtifactRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='buildstream.v2.UpdateArtifactRequest.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cache_key', full_name='buildstream.v2.UpdateArtifactRequest.cache_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='artifact', full_name='buildstream.v2.UpdateArtifactRequest.artifact', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=808,
  serialized_end=917,
)

_ARTIFACT_DEPENDENCY.containing_type = _ARTIFACT
_ARTIFACT_LOGFILE.fields_by_name['digest'].message_type = build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2._DIGEST
_ARTIFACT_LOGFILE.containing_type = _ARTIFACT
_ARTIFACT.fields_by_name['files'].message_type = build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2._DIGEST
_ARTIFACT.fields_by_name['build_deps'].message_type = _ARTIFACT_DEPENDENCY
_ARTIFACT.fields_by_name['public_data'].message_type = build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2._DIGEST
_ARTIFACT.fields_by_name['logs'].message_type = _ARTIFACT_LOGFILE
_ARTIFACT.fields_by_name['buildtree'].message_type = build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2._DIGEST
_UPDATEARTIFACTREQUEST.fields_by_name['artifact'].message_type = _ARTIFACT
DESCRIPTOR.message_types_by_name['Artifact'] = _ARTIFACT
DESCRIPTOR.message_types_by_name['GetArtifactRequest'] = _GETARTIFACTREQUEST
DESCRIPTOR.message_types_by_name['UpdateArtifactRequest'] = _UPDATEARTIFACTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Artifact = _reflection.GeneratedProtocolMessageType('Artifact', (_message.Message,), dict(

  Dependency = _reflection.GeneratedProtocolMessageType('Dependency', (_message.Message,), dict(
    DESCRIPTOR = _ARTIFACT_DEPENDENCY,
    __module__ = 'buildstream.v2.artifact_pb2'
    # @@protoc_insertion_point(class_scope:buildstream.v2.Artifact.Dependency)
    ))
  ,

  LogFile = _reflection.GeneratedProtocolMessageType('LogFile', (_message.Message,), dict(
    DESCRIPTOR = _ARTIFACT_LOGFILE,
    __module__ = 'buildstream.v2.artifact_pb2'
    # @@protoc_insertion_point(class_scope:buildstream.v2.Artifact.LogFile)
    ))
  ,
  DESCRIPTOR = _ARTIFACT,
  __module__ = 'buildstream.v2.artifact_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.Artifact)
  ))
_sym_db.RegisterMessage(Artifact)
_sym_db.RegisterMessage(Artifact.Dependency)
_sym_db.RegisterMessage(Artifact.LogFile)

GetArtifactRequest = _reflection.GeneratedProtocolMessageType('GetArtifactRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETARTIFACTREQUEST,
  __module__ = 'buildstream.v2.artifact_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.GetArtifactRequest)
  ))
_sym_db.RegisterMessage(GetArtifactRequest)

UpdateArtifactRequest = _reflection.GeneratedProtocolMessageType('UpdateArtifactRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEARTIFACTREQUEST,
  __module__ = 'buildstream.v2.artifact_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.UpdateArtifactRequest)
  ))
_sym_db.RegisterMessage(UpdateArtifactRequest)



_ARTIFACTSERVICE = _descriptor.ServiceDescriptor(
  name='ArtifactService',
  full_name='buildstream.v2.ArtifactService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=920,
  serialized_end=1101,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetArtifact',
    full_name='buildstream.v2.ArtifactService.GetArtifact',
    index=0,
    containing_service=None,
    input_type=_GETARTIFACTREQUEST,
    output_type=_ARTIFACT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateArtifact',
    full_name='buildstream.v2.ArtifactService.UpdateArtifact',
    index=1,
    containing_service=None,
    input_type=_UPDATEARTIFACTREQUEST,
    output_type=_ARTIFACT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ARTIFACTSERVICE)

DESCRIPTOR.services_by_name['ArtifactService'] = _ARTIFACTSERVICE

# @@protoc_insertion_point(module_scope)
