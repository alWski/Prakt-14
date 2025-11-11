textLines = []
while True:
    line = input()
    if not line:
        break
    textLines.append(line)

text = " ".join(textLines)

punct = ['.', ',', '!', '?', ';', ':', '(', ')']
words = []
for word in text.split():
    newWord = word.lower()
    for p in punct:
        newWord = newWord.replace(p, '')
    if newWord:
        words.append(newWord)


col = {}
order = []
for word in words:
    if word not in col:
        col[word] = 0
        order.append(word)
    col[word] += 1

for word in sorted(order, key=lambda w: (-col[w], order.index(w))):
    print(word)
