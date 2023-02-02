import re

value = "simp55el#ile&Garn gooK1d"

x = re.findall('\s',value)

print(x)

if x:
    print('values are available')
else:
    print('values are not available')