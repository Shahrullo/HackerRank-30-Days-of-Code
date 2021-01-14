n = int(input())

dic = {}

for i in range(n):
    i = input()
    key = i[:-9]
    value = i[-8:]
    dic[key] = value
    

while True:
    try:
        a = input()
    except EOFError:
        break
    if a in dic:
        print(f'{a}={dic[a]}')
    else:
        print('Not found')     