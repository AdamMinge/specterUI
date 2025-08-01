# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from specterui.proto import specter_pb2 as specterui_dot_proto_dot_specter__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in specterui/proto/specter_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PreviewerServiceStub(object):
    """----------------------------- PreviewerService ---------------------------- //

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListenPreview = channel.unary_stream(
                '/specter_proto.PreviewerService/ListenPreview',
                request_serializer=specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
                response_deserializer=specterui_dot_proto_dot_specter__pb2.PreviewImage.FromString,
                _registered_method=True)


class PreviewerServiceServicer(object):
    """----------------------------- PreviewerService ---------------------------- //

    """

    def ListenPreview(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PreviewerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListenPreview': grpc.unary_stream_rpc_method_handler(
                    servicer.ListenPreview,
                    request_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectId.FromString,
                    response_serializer=specterui_dot_proto_dot_specter__pb2.PreviewImage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'specter_proto.PreviewerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('specter_proto.PreviewerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PreviewerService(object):
    """----------------------------- PreviewerService ---------------------------- //

    """

    @staticmethod
    def ListenPreview(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/specter_proto.PreviewerService/ListenPreview',
            specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
            specterui_dot_proto_dot_specter__pb2.PreviewImage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class MarkerServiceStub(object):
    """------------------------------ MarkerService ------------------------------ //

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Start = channel.unary_unary(
                '/specter_proto.MarkerService/Start',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.Stop = channel.unary_unary(
                '/specter_proto.MarkerService/Stop',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class MarkerServiceServicer(object):
    """------------------------------ MarkerService ------------------------------ //

    """

    def Start(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarkerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'specter_proto.MarkerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('specter_proto.MarkerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MarkerService(object):
    """------------------------------ MarkerService ------------------------------ //

    """

    @staticmethod
    def Start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/specter_proto.MarkerService/Start',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/specter_proto.MarkerService/Stop',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class RecorderServiceStub(object):
    """----------------------------- RecorderService ----------------------------- //

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListenCommands = channel.unary_stream(
                '/specter_proto.RecorderService/ListenCommands',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=specterui_dot_proto_dot_specter__pb2.RecorderCommand.FromString,
                _registered_method=True)


class RecorderServiceServicer(object):
    """----------------------------- RecorderService ----------------------------- //

    """

    def ListenCommands(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecorderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListenCommands': grpc.unary_stream_rpc_method_handler(
                    servicer.ListenCommands,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=specterui_dot_proto_dot_specter__pb2.RecorderCommand.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'specter_proto.RecorderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('specter_proto.RecorderService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class RecorderService(object):
    """----------------------------- RecorderService ----------------------------- //

    """

    @staticmethod
    def ListenCommands(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/specter_proto.RecorderService/ListenCommands',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            specterui_dot_proto_dot_specter__pb2.RecorderCommand.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class ObjectServiceStub(object):
    """----------------------------- ObjectService ------------------------------- //

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTree = channel.unary_unary(
                '/specter_proto.ObjectService/GetTree',
                request_serializer=specterui_dot_proto_dot_specter__pb2.OptionalObjectId.SerializeToString,
                response_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectTree.FromString,
                _registered_method=True)
        self.Find = channel.unary_unary(
                '/specter_proto.ObjectService/Find',
                request_serializer=specterui_dot_proto_dot_specter__pb2.ObjectSearchQuery.SerializeToString,
                response_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectIds.FromString,
                _registered_method=True)
        self.GetObjectQuery = channel.unary_unary(
                '/specter_proto.ObjectService/GetObjectQuery',
                request_serializer=specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
                response_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectSearchQuery.FromString,
                _registered_method=True)
        self.GetParent = channel.unary_unary(
                '/specter_proto.ObjectService/GetParent',
                request_serializer=specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
                response_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectId.FromString,
                _registered_method=True)
        self.GetChildren = channel.unary_unary(
                '/specter_proto.ObjectService/GetChildren',
                request_serializer=specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
                response_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectIds.FromString,
                _registered_method=True)
        self.CallMethod = channel.unary_unary(
                '/specter_proto.ObjectService/CallMethod',
                request_serializer=specterui_dot_proto_dot_specter__pb2.MethodCall.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.UpdateProperty = channel.unary_unary(
                '/specter_proto.ObjectService/UpdateProperty',
                request_serializer=specterui_dot_proto_dot_specter__pb2.PropertyUpdate.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.GetMethods = channel.unary_unary(
                '/specter_proto.ObjectService/GetMethods',
                request_serializer=specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
                response_deserializer=specterui_dot_proto_dot_specter__pb2.Methods.FromString,
                _registered_method=True)
        self.GetProperties = channel.unary_unary(
                '/specter_proto.ObjectService/GetProperties',
                request_serializer=specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
                response_deserializer=specterui_dot_proto_dot_specter__pb2.Properties.FromString,
                _registered_method=True)
        self.ListenTreeChanges = channel.unary_stream(
                '/specter_proto.ObjectService/ListenTreeChanges',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=specterui_dot_proto_dot_specter__pb2.TreeChange.FromString,
                _registered_method=True)
        self.ListenPropertiesChanges = channel.unary_stream(
                '/specter_proto.ObjectService/ListenPropertiesChanges',
                request_serializer=specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
                response_deserializer=specterui_dot_proto_dot_specter__pb2.PropertyChange.FromString,
                _registered_method=True)


class ObjectServiceServicer(object):
    """----------------------------- ObjectService ------------------------------- //

    """

    def GetTree(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Find(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetParent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChildren(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CallMethod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProperty(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMethods(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProperties(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListenTreeChanges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListenPropertiesChanges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObjectServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTree': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTree,
                    request_deserializer=specterui_dot_proto_dot_specter__pb2.OptionalObjectId.FromString,
                    response_serializer=specterui_dot_proto_dot_specter__pb2.ObjectTree.SerializeToString,
            ),
            'Find': grpc.unary_unary_rpc_method_handler(
                    servicer.Find,
                    request_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectSearchQuery.FromString,
                    response_serializer=specterui_dot_proto_dot_specter__pb2.ObjectIds.SerializeToString,
            ),
            'GetObjectQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectQuery,
                    request_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectId.FromString,
                    response_serializer=specterui_dot_proto_dot_specter__pb2.ObjectSearchQuery.SerializeToString,
            ),
            'GetParent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetParent,
                    request_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectId.FromString,
                    response_serializer=specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
            ),
            'GetChildren': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChildren,
                    request_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectId.FromString,
                    response_serializer=specterui_dot_proto_dot_specter__pb2.ObjectIds.SerializeToString,
            ),
            'CallMethod': grpc.unary_unary_rpc_method_handler(
                    servicer.CallMethod,
                    request_deserializer=specterui_dot_proto_dot_specter__pb2.MethodCall.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateProperty': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProperty,
                    request_deserializer=specterui_dot_proto_dot_specter__pb2.PropertyUpdate.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetMethods': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMethods,
                    request_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectId.FromString,
                    response_serializer=specterui_dot_proto_dot_specter__pb2.Methods.SerializeToString,
            ),
            'GetProperties': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProperties,
                    request_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectId.FromString,
                    response_serializer=specterui_dot_proto_dot_specter__pb2.Properties.SerializeToString,
            ),
            'ListenTreeChanges': grpc.unary_stream_rpc_method_handler(
                    servicer.ListenTreeChanges,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=specterui_dot_proto_dot_specter__pb2.TreeChange.SerializeToString,
            ),
            'ListenPropertiesChanges': grpc.unary_stream_rpc_method_handler(
                    servicer.ListenPropertiesChanges,
                    request_deserializer=specterui_dot_proto_dot_specter__pb2.ObjectId.FromString,
                    response_serializer=specterui_dot_proto_dot_specter__pb2.PropertyChange.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'specter_proto.ObjectService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('specter_proto.ObjectService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ObjectService(object):
    """----------------------------- ObjectService ------------------------------- //

    """

    @staticmethod
    def GetTree(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/specter_proto.ObjectService/GetTree',
            specterui_dot_proto_dot_specter__pb2.OptionalObjectId.SerializeToString,
            specterui_dot_proto_dot_specter__pb2.ObjectTree.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Find(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/specter_proto.ObjectService/Find',
            specterui_dot_proto_dot_specter__pb2.ObjectSearchQuery.SerializeToString,
            specterui_dot_proto_dot_specter__pb2.ObjectIds.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetObjectQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/specter_proto.ObjectService/GetObjectQuery',
            specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
            specterui_dot_proto_dot_specter__pb2.ObjectSearchQuery.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetParent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/specter_proto.ObjectService/GetParent',
            specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
            specterui_dot_proto_dot_specter__pb2.ObjectId.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetChildren(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/specter_proto.ObjectService/GetChildren',
            specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
            specterui_dot_proto_dot_specter__pb2.ObjectIds.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CallMethod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/specter_proto.ObjectService/CallMethod',
            specterui_dot_proto_dot_specter__pb2.MethodCall.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateProperty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/specter_proto.ObjectService/UpdateProperty',
            specterui_dot_proto_dot_specter__pb2.PropertyUpdate.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetMethods(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/specter_proto.ObjectService/GetMethods',
            specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
            specterui_dot_proto_dot_specter__pb2.Methods.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetProperties(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/specter_proto.ObjectService/GetProperties',
            specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
            specterui_dot_proto_dot_specter__pb2.Properties.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListenTreeChanges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/specter_proto.ObjectService/ListenTreeChanges',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            specterui_dot_proto_dot_specter__pb2.TreeChange.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListenPropertiesChanges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/specter_proto.ObjectService/ListenPropertiesChanges',
            specterui_dot_proto_dot_specter__pb2.ObjectId.SerializeToString,
            specterui_dot_proto_dot_specter__pb2.PropertyChange.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
