# 在Python中需要自己处理key排序的问题。
v4 = {
    "aid": 123,
    "xx": 999,
    "wid": 888
}

# 1.python 根据key进行排序
# data = ["{}={}".format(key,v4[key])  for key in sorted(v4.keys())]

# 2.再进行拼接
# result = "&".join(data)

result = "&".join(["{}={}".format(key, v4[key]) for key in sorted(v4.keys())])
print(result)
