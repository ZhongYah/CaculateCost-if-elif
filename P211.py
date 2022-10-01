#輸入
id = input('文字:')

amount = input('人數')
amount = int(amount)

#判斷
if id in ['A', 'C', 'E', 'F', 'K']: #list 清單
     total = 350*amount
else:
     total = 550*amount


print(f'{total: ,}元')
 