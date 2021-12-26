import time

import grpc
import test_pb2_grpc as pb2_grpc
import test_pb2 as pb2

def gen(serial, status):
  return send(serial, status)

def send(serial, status):
  yield pb2.ControlGateRequest(
      serial=serial, gate_status=f"status: {status}")

status = ""

channel = grpc.insecure_channel('127.0.0.1:9004')
stub = pb2_grpc.TestStub(channel)
print("connected to server")
while True:
  try:
    for r in stub.ControlGate(gen("dk_serial", status)):
      print(r)
      status = r.control
  except grpc._channel._Rendezvous as err:
    print(err)
    # channel = grpc.insecure_channel('127.0.0.1:9004')
    stub = pb2_grpc.TestStub(channel)
    print("reconnected to server")
  time.sleep(3)



"""
edge <=> server

server OpenGate => client
edge status => server


"""