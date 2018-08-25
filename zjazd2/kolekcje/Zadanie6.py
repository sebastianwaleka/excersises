# Napisz program zamieniejaący miejscami w zadanej ilości liczb element największy z najmniejszym

list = [5, 2, 1, 4, 3]

# Wersja bez użycia pętli for
# print(list)
# max_index = list.index(max(list))
# min_index = list.index(min(list))
#
# max = max(list)
# min = min(list)
#
# list[max_index] = min
# list[min_index] = max
# print(list)
# -----------------------------------------------------
# Wersja z użyciem pętli for do odszukania min i max.
print(f'Original version of: {list}')
# count = 0
# # indexes = []
# min_ = float('Inf')
# max_ = float('-Inf')
min_ = None
max_ = None
# for i in list:
#     indexes.append(count)
#     count += 1
# !!!!!!!! po zastosowaniu range(len(list)) niepotrzebne są inne liczniki
# Poniżej wersja, jeśli min_ i max_ miały wartości początkowe None.
for i in range(len(list)):
    if min_ is None or list[i] < min_:
        min_ = list[i]
    if max_ is None or list[i] > max_:
        max_ = list[i]
# for i in range(len(list)):
#     if list[i] > max_:
#         max_ = list[i]
#     elif list[i] < min_:
#         min_ = list[i]

max_index = list.index(max_)
min_index = list.index(min_)
list[max_index] = min_
list[min_index] = max_
print(f'List after changing max position with min position: {list}')
