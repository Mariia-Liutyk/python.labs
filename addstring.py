# A
def n_indic(a):
    print(a[::2])

b = [1, 2, 3, 4, 5]
n_indic(b)

# B
def even_element(number):
    numbers = []
    for num in number:
       if num %2 == 0:
           numbers.append(num)
    print(numbers)

lst_even_el = [1, 2, 3, 4, 5, 6, 7, 8]
even_element(lst_even_el)

# C (Більше попереднього)
def more_number(lst):
    greater = [item[1] for item in filter(lambda x: x[1] > x[0], zip(lst, lst[1:]))]
    print(greater)

vam = [1, 4, 2, 6, 3, 8]
more_number(vam)

# D
def positiv_num_index(d_index):
    pos = list(map(lambda x: x[0], filter(lambda x: x[1] > 0, enumerate(d_index))))
    print(pos)

posit = [2, -1, 0, 2, -3, 4 , -5, 7, 8]
positiv_num_index(posit)

# E
def positiv_num_index2(d_index2):
    pos2 = list(map(lambda x: x[0], filter(lambda x: x[1] > 0, enumerate(d_index2))))
    return pos2 or [-1]

posit2 = [-1, 0, 2]
posit3 = [0]
print(positiv_num_index2(posit2))
print(positiv_num_index2(posit3))

# F
def max_num(f_num):
    return max(f_num), f_num.index(max(f_num))

f = [1, 3, 2, 4, 5, 5]
print(max_num(f))

print('G')
def count_elements(numbers):
    count = 0
    for i in range(1, len(numbers)-1):
        if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
            count += 1
    return count

g = [1, 0, 1, 0, 1,]
print(count_elements(g))

print('H')
def min_value(h_num):
    return min(i for i in h_num if i > 0)

h = [-3, 2, 4, -5]
print(min_value(h))

print('I')
def closest(lst_I, x):
    return min(lst_I, key=lambda i: abs(i - x))

lst_I = [6, 5, 4, 2, 1]
x = 3
print(closest(lst_I, x))

lst_I = [1, 2, 4, 5, 6]
x = 3
print(closest(lst_I, x))

lst_I = [1, 2, 3]
x = 2
print(closest(lst_I, x))

print('J')
def find_position(heights, x):
    position = 1
    while position <= len(heights) and heights[position - 1] >= x:
        position += 1
    return position

heights = [165, 163, 160, 160, 157, 157, 155, 154]
x = 162
print(find_position(heights, x))

print("K")
def search_number(num_k):
    return len(set(num_k))

k = [1, 2, 2, 3, 3, 3]
print(search_number(k))

print('L')
def small_odd(lst):
    odds = [x for x in lst if x % 2 != 0]
    if odds:
        return min(odds)
    else:
        return 0

l = [0, 1, 2, 3, 4]
print(small_odd(l))

l_1 = [2, 4, 6, 8, 10]
print(small_odd(l_1))

print('M')
def reverse_list(lst_2):
    n = len(lst_2)
    for i in range(n // 2):
        lst_2[i], lst_2[n - 1 - i] = lst_2[n - 1 - i], lst_2[i]
    return lst_2

m = [1, 2, 3, 4, 5]
print(reverse_list(m))

print('N')
def swap_adjacent_elements(N_lst):
    for i in range(0, len(N_lst) - 1, 2):
        N_lst[i], N_lst[i+1] = N_lst[i+1], N_lst[i]
    return N_lst

n = [1, 2 ,3, 4, 5]
print(swap_adjacent_elements(n))

print('O')
def swap_min_max(lst):
    min_val = min(lst)
    max_val = max(lst)
    for i in range(len(lst)):
        if lst[i] == min_val:
            lst[i] = max_val
        elif lst[i] == max_val:
            lst[i] = min_val
    return lst

print("R")
def count_pairs(nums):
  counts = {}
  for num in nums:
    if num in counts:
      counts[num] += 1
    else:
      counts[num] = 1
  pairs = 0
  for count in counts.values():
    if count >= 2:
      pairs += count * (count - 1) // 2
  return pairs

r1 = [1, 2, 3, 2, 3, 2]
r = [1, 1, 1, 1, 1]
print(count_pairs(r))
print(count_pairs(r1))

print("T")
def different_el(elements):
    elem = set()
    for element in elements:
        elem.add(element)
    return len(elem)

t2 = [3, 2, 1, 2, 3]
print(different_el(t2))

print('V')
def unique_lst(v_lst):
    count = {}
    for v in v_lst:
        if v in count:
            count[v] += 1
        else:
            count[v] = 1
    for v in v_lst:
        if count[v] == 1:
            return v

ls = [1, 2, '+', 3, 3, 3]
print(unique_lst(ls))