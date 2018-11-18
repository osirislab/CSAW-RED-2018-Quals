# Description

Cant decide if I think a p is an upside down b or a b is an upside down p.

200 pts

# Deploying

Runs on port 8000 inside container

$ docker build -t adhd .
$ docker run -it -p <outerport>:8000 adhd

# Challenge

Small PIE binary to teach properties of PIE binaries.
Specifically that the bottom three nibbles of the binary always stay the same no matter what.

# Tested? ✓

### Tested locally

$ python solve.py -b pibolar

This will just print out the flag

### Tested remotely (locally) ✓

$ python solve.py -r <remoteaddr> -p <port> -e libc.so.6
$ cat flag.txt

### Not deployed yet