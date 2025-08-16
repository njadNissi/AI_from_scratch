
fw = open('sample.txt', 'w')
fw.write('writing rubbish just for test\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
fr.close()
print(text)