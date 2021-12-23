# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import test_pb2 as test__pb2


class TestStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ControlGate = channel.stream_stream(
                '/test.Test/ControlGate',
                request_serializer=test__pb2.ControlGateRequest.SerializeToString,
                response_deserializer=test__pb2.ControlGateResponse.FromString,
                )


class TestServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ControlGate(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TestServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ControlGate': grpc.stream_stream_rpc_method_handler(
                    servicer.ControlGate,
                    request_deserializer=test__pb2.ControlGateRequest.FromString,
                    response_serializer=test__pb2.ControlGateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'test.Test', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Test(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ControlGate(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/test.Test/ControlGate',
            test__pb2.ControlGateRequest.SerializeToString,
            test__pb2.ControlGateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
