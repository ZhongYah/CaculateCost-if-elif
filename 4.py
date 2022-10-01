a = (0, 1, 3, '8')
print(a)
print(a[2])
# a[2] = 5  錯，tuple是immutable物件 當初值設定後就不可更改
print(type(a))