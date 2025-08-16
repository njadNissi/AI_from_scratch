import random as rd

intro = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
main_char = [' there lived a king.',
             ' there was a man named Jack.', ' there lived a farmer.']
time = [' One day', ' One full-moon night']
plot = [' he was passing by', ' he was going for a picnic to ']
place = [' the mountains', ' the garden']
second_char = [' he saw a man', ' he saw a young lady']
age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
work = [' searching something.', ' digging a well on roadside.']


def tell():
    print(rd.choice(intro) + rd.choice(main_char) + rd.choice(time) + rd.choice(plot) +
          rd.choice(place) + rd.choice(second_char) + rd.choice(age) + rd.choice(work))


tell()
