# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from service_protos import launcher_service_pb2 as service__protos_dot_launcher__service__pb2


class LauncherServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Restart = channel.unary_unary(
                '/service_manager.LauncherService/Restart',
                request_serializer=service__protos_dot_launcher__service__pb2.NodeCollection.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Start = channel.unary_unary(
                '/service_manager.LauncherService/Start',
                request_serializer=service__protos_dot_launcher__service__pb2.NodeCollection.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Stop = channel.unary_unary(
                '/service_manager.LauncherService/Stop',
                request_serializer=service__protos_dot_launcher__service__pb2.NodeCollection.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Status = channel.unary_unary(
                '/service_manager.LauncherService/Status',
                request_serializer=service__protos_dot_launcher__service__pb2.NodeCollection.SerializeToString,
                response_deserializer=service__protos_dot_launcher__service__pb2.NodeStatusCollection.FromString,
                )
        self.Log = channel.unary_unary(
                '/service_manager.LauncherService/Log',
                request_serializer=service__protos_dot_launcher__service__pb2.LogContext.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Options = channel.unary_unary(
                '/service_manager.LauncherService/Options',
                request_serializer=service__protos_dot_launcher__service__pb2.Option.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.OrinStatus = channel.unary_unary(
                '/service_manager.LauncherService/OrinStatus',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=service__protos_dot_launcher__service__pb2.OneOrinStatus.FromString,
                )
        self.SetParam = channel.unary_unary(
                '/service_manager.LauncherService/SetParam',
                request_serializer=service__protos_dot_launcher__service__pb2.ParamServer.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetParam = channel.unary_unary(
                '/service_manager.LauncherService/GetParam',
                request_serializer=service__protos_dot_launcher__service__pb2.ParamServer.SerializeToString,
                response_deserializer=service__protos_dot_launcher__service__pb2.ParamServer.FromString,
                )
        self.ListParam = channel.unary_unary(
                '/service_manager.LauncherService/ListParam',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=service__protos_dot_launcher__service__pb2.ParamServerList.FromString,
                )


class LauncherServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Restart(self, request, context):
        """Restarts a list of onboard nodes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Start(self, request, context):
        """Starts a list of onboard nodes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """Stops a list of onboard nodes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Log(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Options(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrinStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetParam(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetParam(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListParam(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LauncherServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Restart': grpc.unary_unary_rpc_method_handler(
                    servicer.Restart,
                    request_deserializer=service__protos_dot_launcher__service__pb2.NodeCollection.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=service__protos_dot_launcher__service__pb2.NodeCollection.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=service__protos_dot_launcher__service__pb2.NodeCollection.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Status': grpc.unary_unary_rpc_method_handler(
                    servicer.Status,
                    request_deserializer=service__protos_dot_launcher__service__pb2.NodeCollection.FromString,
                    response_serializer=service__protos_dot_launcher__service__pb2.NodeStatusCollection.SerializeToString,
            ),
            'Log': grpc.unary_unary_rpc_method_handler(
                    servicer.Log,
                    request_deserializer=service__protos_dot_launcher__service__pb2.LogContext.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Options': grpc.unary_unary_rpc_method_handler(
                    servicer.Options,
                    request_deserializer=service__protos_dot_launcher__service__pb2.Option.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'OrinStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.OrinStatus,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=service__protos_dot_launcher__service__pb2.OneOrinStatus.SerializeToString,
            ),
            'SetParam': grpc.unary_unary_rpc_method_handler(
                    servicer.SetParam,
                    request_deserializer=service__protos_dot_launcher__service__pb2.ParamServer.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetParam': grpc.unary_unary_rpc_method_handler(
                    servicer.GetParam,
                    request_deserializer=service__protos_dot_launcher__service__pb2.ParamServer.FromString,
                    response_serializer=service__protos_dot_launcher__service__pb2.ParamServer.SerializeToString,
            ),
            'ListParam': grpc.unary_unary_rpc_method_handler(
                    servicer.ListParam,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=service__protos_dot_launcher__service__pb2.ParamServerList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'service_manager.LauncherService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LauncherService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Restart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service_manager.LauncherService/Restart',
            service__protos_dot_launcher__service__pb2.NodeCollection.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/service_manager.LauncherService/Start',
            service__protos_dot_launcher__service__pb2.NodeCollection.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/service_manager.LauncherService/Stop',
            service__protos_dot_launcher__service__pb2.NodeCollection.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service_manager.LauncherService/Status',
            service__protos_dot_launcher__service__pb2.NodeCollection.SerializeToString,
            service__protos_dot_launcher__service__pb2.NodeStatusCollection.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Log(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service_manager.LauncherService/Log',
            service__protos_dot_launcher__service__pb2.LogContext.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Options(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service_manager.LauncherService/Options',
            service__protos_dot_launcher__service__pb2.Option.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrinStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service_manager.LauncherService/OrinStatus',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            service__protos_dot_launcher__service__pb2.OneOrinStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetParam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service_manager.LauncherService/SetParam',
            service__protos_dot_launcher__service__pb2.ParamServer.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetParam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service_manager.LauncherService/GetParam',
            service__protos_dot_launcher__service__pb2.ParamServer.SerializeToString,
            service__protos_dot_launcher__service__pb2.ParamServer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListParam(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/service_manager.LauncherService/ListParam',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            service__protos_dot_launcher__service__pb2.ParamServerList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
