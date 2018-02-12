import sys
import os
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
print "------------------------"


# writes the protobuf stream on a binary file on disk
with open('generatedOutputMessage.bin', 'wb') as f:
    f.write(person.SerializeToString())

# display the size of the written file
statinfo = os.stat('generatedOutputMessage.bin')
print statinfo.st_size

# here we check, if we can read the just dumped data
with open('generatedOutputMessage.bin', 'rb') as f:
    person = addressbook_pb2.Person()
    person.ParseFromString(f.read())

print person.name
