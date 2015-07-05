text = '''aaaaaa aaaaaa aaaa aaaa a aa aa a aa0
bbbbbb bbbbbb bbbbbbbbbb.ccc ccccc c0
dddd ddddd ddddd.eeeee eeeeeee.fffff0
fffff fff ffffff.ggg ggg gg g.eeefaa0.'''

lines = list(text.split('\n'))
words = list(text.split(' '))
sentenses = list(text.split('.'))

print(len(lines), lines, '\n')
print(len(words), words, '\n')
print(len(sentenses), sentenses, '\n')
print(len(text))
