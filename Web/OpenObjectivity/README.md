## Open Individualism

# Description
In the end aren't we all the same anyway?

# Challenge
500 points

flag{p3rson@l_1den7ity_is_A_m3Me}

Admin is created on startup, therefore ID is 1. Leaking SECRET_KEY
would allow for signing your own admin tokens. Send 'Config' as clicker name
and 'SECRET_KEY' as field to leak out SECRET_KEY. Admins have access to endpoints
that allow for incrementing money and uuid's of users. Uuids can be predicted once
the random seed is leaked out. Send 'Config' as clicker name and 'SEED' as field
to leek out the seed of random used for creating uuids. Create around 14 users.
Max out money and buy captiosus click 10 times for each user. Find
the ids of each user through decoding auth token. Ids indicate how long to random until
you get your own uuid. Find largest uuid value and increase each user's uuid until
they match. Send requests from each account in a loop (it'll probably be slow enough
to not trigger the rate limit ban). Once 5 seconds have passed, break loop
and check record endpoint for flag.


# Tested
solver.py also has some tests that I ran
