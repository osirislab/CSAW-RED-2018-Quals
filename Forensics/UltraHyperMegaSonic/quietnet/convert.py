from base64 import b64encode
import send


def to_base(n, base=3):
    if n == 0:
        return 0
    remainders = []
    while n:
        n, remainder = divmod(n,base)
        remainders.append(str(remainder))
    
    num_zeros = 6 - len(remainders)
    for i in range(num_zeros):
        remainders.append(str(0))
    return "".join(remainders[::-1])

def converter(filename):
    contents = ""
    int_contents = []
    tern_contents = []
    with open(filename, 'rb') as infile:
        contents = infile.read()
    contents = b64encode(contents)
    for c in contents:
        tern_contents.append(to_base(c, 3))
    return tern_contents

make_buffer = send.make_custom_buffer_from_bit_pattern
transmit = send.play_buffer

def make_sounds(contents):
    joined_contents = "x".join(contents)
    with open('verify', 'w') as out:
        out.write(joined_contents)
    buffer = make_buffer(joined_contents)
    transmit(buffer)


cont = converter("flag")
make_sounds(cont)
