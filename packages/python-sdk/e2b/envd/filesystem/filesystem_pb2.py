# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filesystem/filesystem.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from e2b.envd.permissions import permissions_pb2 as permissions_dot_permissions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1b\x66ilesystem/filesystem.proto\x12\nfilesystem\x1a\x1dpermissions/permissions.proto"n\n\x0bMoveRequest\x12\x16\n\x06source\x18\x01 \x01(\tR\x06source\x12 \n\x0b\x64\x65stination\x18\x02 \x01(\tR\x0b\x64\x65stination\x12%\n\x04user\x18\x03 \x01(\x0b\x32\x11.permissions.UserR\x04user"\x0e\n\x0cMoveResponse"K\n\x0eMakeDirRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12%\n\x04user\x18\x02 \x01(\x0b\x32\x11.permissions.UserR\x04user"\x11\n\x0fMakeDirResponse"J\n\rRemoveRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12%\n\x04user\x18\x02 \x01(\x0b\x32\x11.permissions.UserR\x04user"\x10\n\x0eRemoveResponse"H\n\x0bStatRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12%\n\x04user\x18\x02 \x01(\x0b\x32\x11.permissions.UserR\x04user";\n\x0cStatResponse\x12+\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x15.filesystem.EntryInfoR\x05\x65ntry"I\n\tEntryInfo\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x14.filesystem.FileTypeR\x04type"K\n\x0eListDirRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12%\n\x04user\x18\x02 \x01(\x0b\x32\x11.permissions.UserR\x04user"B\n\x0fListDirResponse\x12/\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x15.filesystem.EntryInfoR\x07\x65ntries"L\n\x0fWatchDirRequest\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12%\n\x04user\x18\x02 \x01(\x0b\x32\x11.permissions.UserR\x04user"\xe1\x02\n\x10WatchDirResponse\x12?\n\x05start\x18\x01 \x01(\x0b\x32\'.filesystem.WatchDirResponse.StartEventH\x00R\x05start\x12N\n\nfilesystem\x18\x02 \x01(\x0b\x32,.filesystem.WatchDirResponse.FilesystemEventH\x00R\nfilesystem\x12\x46\n\tkeepalive\x18\x03 \x01(\x0b\x32&.filesystem.WatchDirResponse.KeepAliveH\x00R\tkeepalive\x1a\x0c\n\nStartEvent\x1aP\n\x0f\x46ilesystemEvent\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x15.filesystem.EventTypeR\x04type\x1a\x0b\n\tKeepAliveB\x07\n\x05\x65vent*R\n\x08\x46ileType\x12\x19\n\x15\x46ILE_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x46ILE_TYPE_FILE\x10\x01\x12\x17\n\x13\x46ILE_TYPE_DIRECTORY\x10\x02*\x98\x01\n\tEventType\x12\x1a\n\x16\x45VENT_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11\x45VENT_TYPE_CREATE\x10\x01\x12\x14\n\x10\x45VENT_TYPE_WRITE\x10\x02\x12\x15\n\x11\x45VENT_TYPE_REMOVE\x10\x03\x12\x15\n\x11\x45VENT_TYPE_RENAME\x10\x04\x12\x14\n\x10\x45VENT_TYPE_CHMOD\x10\x05\x32\x94\x03\n\nFilesystem\x12\x39\n\x04Stat\x12\x17.filesystem.StatRequest\x1a\x18.filesystem.StatResponse\x12\x42\n\x07MakeDir\x12\x1a.filesystem.MakeDirRequest\x1a\x1b.filesystem.MakeDirResponse\x12\x39\n\x04Move\x12\x17.filesystem.MoveRequest\x1a\x18.filesystem.MoveResponse\x12\x42\n\x07ListDir\x12\x1a.filesystem.ListDirRequest\x1a\x1b.filesystem.ListDirResponse\x12G\n\x08WatchDir\x12\x1b.filesystem.WatchDirRequest\x1a\x1c.filesystem.WatchDirResponse0\x01\x12?\n\x06Remove\x12\x19.filesystem.RemoveRequest\x1a\x1a.filesystem.RemoveResponseBi\n\x0e\x63om.filesystemB\x0f\x46ilesystemProtoP\x01\xa2\x02\x03\x46XX\xaa\x02\nFilesystem\xca\x02\nFilesystem\xe2\x02\x16\x46ilesystem\\GPBMetadata\xea\x02\nFilesystemb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "filesystem.filesystem_pb2", _globals
)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\016com.filesystemB\017FilesystemProtoP\001\242\002\003FXX\252\002\nFilesystem\312\002\nFilesystem\342\002\026Filesystem\\GPBMetadata\352\002\nFilesystem"
    _globals["_FILETYPE"]._serialized_start = 1181
    _globals["_FILETYPE"]._serialized_end = 1263
    _globals["_EVENTTYPE"]._serialized_start = 1266
    _globals["_EVENTTYPE"]._serialized_end = 1418
    _globals["_MOVEREQUEST"]._serialized_start = 74
    _globals["_MOVEREQUEST"]._serialized_end = 184
    _globals["_MOVERESPONSE"]._serialized_start = 186
    _globals["_MOVERESPONSE"]._serialized_end = 200
    _globals["_MAKEDIRREQUEST"]._serialized_start = 202
    _globals["_MAKEDIRREQUEST"]._serialized_end = 277
    _globals["_MAKEDIRRESPONSE"]._serialized_start = 279
    _globals["_MAKEDIRRESPONSE"]._serialized_end = 296
    _globals["_REMOVEREQUEST"]._serialized_start = 298
    _globals["_REMOVEREQUEST"]._serialized_end = 372
    _globals["_REMOVERESPONSE"]._serialized_start = 374
    _globals["_REMOVERESPONSE"]._serialized_end = 390
    _globals["_STATREQUEST"]._serialized_start = 392
    _globals["_STATREQUEST"]._serialized_end = 464
    _globals["_STATRESPONSE"]._serialized_start = 466
    _globals["_STATRESPONSE"]._serialized_end = 525
    _globals["_ENTRYINFO"]._serialized_start = 527
    _globals["_ENTRYINFO"]._serialized_end = 600
    _globals["_LISTDIRREQUEST"]._serialized_start = 602
    _globals["_LISTDIRREQUEST"]._serialized_end = 677
    _globals["_LISTDIRRESPONSE"]._serialized_start = 679
    _globals["_LISTDIRRESPONSE"]._serialized_end = 745
    _globals["_WATCHDIRREQUEST"]._serialized_start = 747
    _globals["_WATCHDIRREQUEST"]._serialized_end = 823
    _globals["_WATCHDIRRESPONSE"]._serialized_start = 826
    _globals["_WATCHDIRRESPONSE"]._serialized_end = 1179
    _globals["_WATCHDIRRESPONSE_STARTEVENT"]._serialized_start = 1063
    _globals["_WATCHDIRRESPONSE_STARTEVENT"]._serialized_end = 1075
    _globals["_WATCHDIRRESPONSE_FILESYSTEMEVENT"]._serialized_start = 1077
    _globals["_WATCHDIRRESPONSE_FILESYSTEMEVENT"]._serialized_end = 1157
    _globals["_WATCHDIRRESPONSE_KEEPALIVE"]._serialized_start = 1159
    _globals["_WATCHDIRRESPONSE_KEEPALIVE"]._serialized_end = 1170
    _globals["_FILESYSTEM"]._serialized_start = 1421
    _globals["_FILESYSTEM"]._serialized_end = 1825
# @@protoc_insertion_point(module_scope)
