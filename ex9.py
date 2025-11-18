def proc_text():
    text_lines = []
    while True:
        line = input()
        if not line:
            break
        text_lines.append(line)

    text = " ".join(text_lines)

    punct = ['.', ',', '!', '?', ';', ':', '(', ')']
    words = []
    for word in text.split():
        new_word = word.lower()
        for p in punct:
            new_word = new_word.replace(p, '')
        if new_word:
            words.append(new_word)

    col = {}
    order = []
    for word in words:
        if word not in col:
            col[word] = 0
            order.append(word)
        col[word] += 1

    result = []
    for word in sorted(order, key=lambda w: (-col[w], order.index(w))):
        result.append(word)
    
    return result
    
def main():
    result = proc_text()
    for word in result:
        print(word)

if __name__ == "__main__":
    main()
