MAX = 10000

for i in range(MAX): # list of tasks
    for j in range(MAX): # the i task to accomplish
        k = i * j
    print(f'{i + 1} / {MAX}', end='\r')
print('progress finished!')