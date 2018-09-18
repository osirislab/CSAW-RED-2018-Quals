# Description

So many voices but only one to choose from

# Deploying

Runs on port 8000 inside container

$ docker build -t adhd .
$ docker run -it -p <outerport>:8000 adhd

# Challenge ✓

Single null-byte poison
As textbook as you can get it
Basically they just have to consolidate the heap over a thing,
overwrite it with print_flag fn, and call fidget on it to print flag.

No need for libc or popping shell! (even tho they could)

# Tested?

### Tested locally ✓

$ python solve.py -b pibolar

This will just print out the flag

### Tested remotely (locally) ✓

$ python solve.py -r <remoteaddr> -p <port> -e libc.so.6
$ cat flag.txt

### Not deployed yet