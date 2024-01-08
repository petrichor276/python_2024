byte_list = [-49, -60, -62, -27]

bs = bytearray()  # python字节数组
for item in byte_list:
    if item < 0:
        item = item + 256
    bs.append(item)

str_data = bs.decode('gbk')  # data = bytes(bs)
print(str_data)
