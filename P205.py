from struct import pack


pack = input('')

amount = input('')

amount = int(amount)

if    pack == 'A':
      total = 155*amount
elif  pack == 'B':
      total = 165*amount
elif  pack == 'C':
      total = 175*amount
elif  pack == 'D':
      total = 185*amount

print(f'{total: ,}元')
