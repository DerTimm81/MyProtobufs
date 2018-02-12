
Please call

protoc -I=. --python_out=./protobuf_out addressbook.proto

to compile the protobuf.

After successful compilation, call the python script, that makes use of the compiled protobuf by calling:

python check_addressbook.py
