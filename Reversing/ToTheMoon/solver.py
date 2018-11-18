import hashlib

goal = "flag{WH4T_MONEY}"
print 'GOAL HASH IS', hashlib.sha1(goal).hexdigest()

your_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ4'
complete_list = []
for current in xrange(4):
    a = [i for i in your_list]
    for y in xrange(current):
        a = [x+i for i in your_list for x in a]
    complete_list = complete_list+a


for i in complete_list:
    if hashlib.sha1("flag{"+i+"_MONEY}").hexdigest() == '461f168de32239db6e3cfee433ea59a8d5cd5ec3':
        print i
        print 'done'
