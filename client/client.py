import time

import grpc
import test_pb2_grpc as pb2_grpc
import test_pb2 as pb2


def gen():
  while True:
    i = input("\nEnter a number or 'q' to quit: \n")
    if i == "q":
      break
    try:
      num = int(i)
    except ValueError:
      continue
    yield pb2.ControlGateRequest(
      serial="serial123", gate_status=f"status {num}")

    time.sleep(0.1)

channel = grpc.insecure_channel('127.0.0.1:9004')
stub = pb2_grpc.TestStub(channel)
it = stub.ControlGate(gen())

while True:
  try:
    for r in it:
      print(r)
  except grpc._channel._Rendezvous as err:
    print(err)
    time.sleep(3)
