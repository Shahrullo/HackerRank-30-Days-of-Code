n = int(input())

for i in range(n):
    i = int(input())
    if i == 1:
        print('Not prime')
    else:
        if i % 2 == 0 and i > 2:
            print('Not prime')
        else:
            for j in range(3, int(i**(1/2))+1, 2):
                if i % j == 0:
                    print('Not prime')
                    break
            else:
                print('Prime')