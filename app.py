# for loop

'''
for i in range(1, 10):
    print(i)
'''

'''
phones = ['xiaomi', 'iphone6', 'samsung']

for phone in phones:
    print(phone)
'''

phones = [
    {"id": 1, "name": "xiaomi"},
    {"id": 2, "name": "iphone6"},
    {"id": 3, "name": "samsung"}
]

for phone in phones:
    print(phone['name'])
