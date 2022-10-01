#輸入
id = input('身分證:')

#最後一碼
m = id[-1]

#判斷
if m == '0' or m == '4' or m == '3':
     print('中獎')
else:
     print('沒中獎')

#判斷(1)
if m  in ('0', '2', '3'): #tuple 元組
     print('中獎')
else:
     print('沒中獎')

#判斷(2)
if m in ['1', '5', '8']: #list 清單
     print('中獎')
else:
     print('沒中獎')


