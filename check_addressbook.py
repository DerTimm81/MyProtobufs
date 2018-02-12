import sys
from protobuf_out import addressbook_pb2
# from protobuf-3.5.1 import python

print "Hello."

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

print person.id
