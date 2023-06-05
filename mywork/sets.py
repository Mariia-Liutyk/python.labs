# A
def diverse(lst_diverse_num):
    return len(set(lst_diverse_num))


print(diverse([1, 2, 3, 4, 1]))

# B
def count_num(lst_1, lst_2):
    return len(set(lst_1).intersection(set(lst_2)))


lst_1 = [1, 2, 3]
lst_2 = [4, 3, 2]
result = count_num(lst_1, lst_2)
print(result)

# C
def crossing_lists(lst1, lst2):
    return sorted(set(lst1) & set(lst2))

lst1 = [1, 2, 3]
lst2 = [5, 3, 2]
res = crossing_lists(lst1, lst2)
print(res)

# D
def check_duplicates(sequence):
    seen_numbers = set()
    for number in sequence:
        if number in seen_numbers:
            print("YES")
        else:
            print("NO")
            seen_numbers.add(number)

sequence = [1, 2, 3, 2, 3, 4]
check_duplicates(sequence)

# E
def find_common_colors(n, m, iryna_colors, igor_colors):
    common_colors = sorted(set(iryna_colors) & set(igor_colors))
    iryna_unique = sorted(set(iryna_colors) - set(common_colors))
    igor_unique = sorted(set(igor_colors) - set(common_colors))
    print(len(common_colors), *common_colors)
    print(len(iryna_unique), *iryna_unique)
    print(len(igor_unique), *igor_unique)

n = 4
m = 3
iryna_colors = [0, 1, 10, 9]
igor_colors = [1, 3, 0]
find_common_colors(n, m, iryna_colors, igor_colors)

# F
def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

with open('F.txt', 'r') as file:
    text = file.read()

result = count_unique_words(text)
print(result)

# G
def guess_number(n, queries):
    possible_numbers = set(range(1, n + 1))
    for query in queries:
        numbers, answer = query
        if answer == 'YES':
            possible_numbers &= set(numbers)
        else:
            possible_numbers -= set(numbers)
    return sorted(list(possible_numbers))

n = 10
queries = [([1, 2, 3, 4, 5], 'YES'), ([2, 4, 6, 8, 10], 'NO')]
print(guess_number(n, queries))