# Description

Jumpy jump?

# Deploying

Runs on port 8000 inside container

# Challenge

ROPChain similar to dinner_time, but without /bin/sh string in memory
Also full RELRO so they have to leak libc and actually retrieve environ,
giving them stack and a ptr to controlled input (where they will put /bin/sh)

The ROPChain starts right away as well (while also cleaning up registers),
so they have to take into account the cleared registers as well.

# Tested?

### Tested locally

$ python solve.py -b adhd -e libc.so.6
$ cat flag.txt

### Tested 

$ python solve.py -r <remoteaddr> -p <port> -e libc.so.6
$ cat flag.txt