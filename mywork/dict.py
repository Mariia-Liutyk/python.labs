# K
def count_words(txt):
    word_count = {}
    words = txt.split()
    for word in words:
        if word not in word_count:
            word_count[word] = 0
        print(word_count[word], end=' ')
        word_count[word] += 1

with open('k.txt', 'r') as file:
    txt = file.read()

res = count_words(txt)
print(res)

# L
def find_synonym(synonyms, word):
    for synonym_pair in synonyms:
        if word in synonym_pair:
            synonym_pair.remove(word)
            return synonym_pair[0]

with open("L.txt", "r") as file:
    n = int(file.readline().strip())
    synonyms = []
    for _ in range(n):
        synonym_pair = file.readline().strip().split()
        synonyms.append(synonym_pair)
    word = file.readline().strip()

synonym = find_synonym(synonyms, word)
print(synonym)

# N
def find_most_frequent_word(file_path):
    with open(file_path, 'r') as file:
        text = file.read().replace('\n', '')

    # Розділяємо текст на слова
    words = text.split()

    # Рахуємо кількість входжень кожного слова
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    max_count = max(word_counts.values())
    most_frequent_words = [word for word, count in word_counts.items() if count == max_count]

    most_frequent_words.sort()
    return most_frequent_words[0]

file_path = 'N.txt'
result = find_most_frequent_word(file_path)
print(result)

