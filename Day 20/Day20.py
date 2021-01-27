
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
n_swaps = 0
for _ in range(n):
    for i in range(n-1):
        if a[i] > a[i+1]:
            n_swaps += 1
            a[i], a[i+1] = a[i+1], a[i]
            
    if n_swaps == 0:
        break
    
print(f'Array is sorted in {n_swaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')