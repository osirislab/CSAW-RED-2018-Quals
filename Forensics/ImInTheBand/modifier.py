import random
image = None

with open('flag.bmp', 'rb') as infile:
    image = bytearray(infile.read())

pixel_offset = image[0x0A:0x0E]

offset = int("".join([str(hex(int(p))).replace('0x', '') for p in pixel_offset[::-1]]), 16)

pixel_array = image[offset:]

for p in range(len(pixel_array)):
    if int(pixel_array[p]) <= 0x64:
        pixel_array[p] = random.randint(0x30,0x90)
    else:
        pixel_array[p] = random.choice((random.randint(0x00, 0x30),random.randint(0x90, 0xff)))


new_img = image[:offset] + pixel_array

with open('output.bmp', 'wb') as outfile:
    outfile.write(new_img)
