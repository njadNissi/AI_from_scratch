MAX = 10000

for i in range(MAX): # list of tasks
    for j in range(MAX): # the i task to accomplish
        k = i * j
    print('Progress:', # □, ■, ▢
          f'|{"■" * ((i + 1) * 50 // MAX):50}|', # :n-> the length of the bar (no of chars)
          f'{(i + 1) * 100 // MAX} %', # show percentage
          end='\r')
print('\nProgress finished!')