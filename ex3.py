s = input()
words = s.split()
res = []

punct = ['.', ',', '!', '?', ';', ':', '(', ')']

for i in words:
    newWord = i

    for j in punct:
        newWord = newWord.replace(j, '')
    if newWord:
        res.append(newWord)

print(res)
