with open('output.bmp', 'rb') as infile:
    image = bytearray(infile.read())

pixel_offset = image[0x0A:0x0E]

offset = int("".join([str(hex(int(p))).replace('0x', '') for p in pixel_offset[::-1]]), 16)

pixel_array = image[offset:]

for p in range(len(pixel_array)):
    if int(pixel_array[p]) <= 0x80 and int(pixel_array[p]) >= 0x40:
        pixel_array[p] = 0xff 
    else:
        pixel_array[p] = 0x00 


new_img = image[:offset] + pixel_array

with open('sol.bmp', 'wb') as outfile:
    outfile.write(new_img)
