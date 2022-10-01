from struct import pack
from tokenize import String


pack = input('')
m = pack[-1]

amount = input('')

amount = int(amount)

if   m  == 'A':
      total = 12.5*amount
elif m  == 'B':
      total = 10.5*amount
elif m  == 'C':
      total = 8.5*amount


print(f'{total: ,.0f}元')
