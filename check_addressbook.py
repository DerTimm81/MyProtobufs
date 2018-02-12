import sys
from protobuf_out import addressbook_pb2

print "Hello."

# initialization
person = addressbook_pb2.Person()

person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"

phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

print "------------------------"
print "OUTPUT:"
print "Name of the person:\t " + person.name
if phone.type is addressbook_pb2.Person.HOME :
    print "Phone number is:\t " + phone.number + " (Home)"
    pass

# print "Given Phone number: " + person.phone.number + "(" + person.phone.type + ")"
print "------------------------"
