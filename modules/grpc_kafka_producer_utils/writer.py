import grpc
import location_pb2
import location_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending example payload...")

channel = grpc.insecure_channel("localhost:30003")
stub = location_pb2_grpc.LocationServiceStub(channel)

# sample payload
location = location_pb2.LocationMessage(
    person_id=5,
    longitude=-76.23489283,
    latitude=832.86789,
    creation_time='2025-04-05 18:22:00'
)


response = stub.Create(location)