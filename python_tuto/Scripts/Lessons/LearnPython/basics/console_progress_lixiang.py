from time import sleep

text = ["李想美女小姐姐，祝你周末愉快，身心健康，考研复试顺利通过.",
"接下来, 请你欣赏AI为你写出来的诗:",
"With eyes like pools of ink so deep,",
"And hair that flows like midnight's sweep,",
"Li Xiang, a beauty to behold,",
"A story waiting to unfold.",
"Her laughter, like a tinkling stream,",
"Her smile, a radiant sunlit beam,",
"A gentle spirit, kind and true,",
"Her grace shines through and through.",
"Like porcelain, her features fine,",
"A heart as warm as summer's wine,",
"With strength that blossoms from within,",
"A spirit that will always win."
"Li Xiang, a friend beyond compare,",
"A treasure precious, ever rare,",
"May friendship's thread forever bind,",
"A bond of beauty, heart, and mind."]


for i in range(len(text)): # list of tasks
    sentence = text[i]
    for j in range(len(sentence)):
        sleep(.25)
        print(f'{sentence[:j]}', end='\r')
    print('\n') # comment this to let sentences substitute older ones.
print('\nProgress finished!')
