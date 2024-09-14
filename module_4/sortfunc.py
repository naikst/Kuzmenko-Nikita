# Несколько алгоритма сортировки


# 1Пузырьковая сортировка (Bubble Sort).  При этом подходе осуществляется перебор по списку и сравнение соседних
# элементов. Они меняются местами в том случае, если порядок неправильный.
# 2 Сортировка выбором (Selection Sort). В
# этом алгоритме список (или массив) делится на две части: список с отсортированными элементами и список с
# элементами, которые только нужно сортировать. Сначала ищется самый маленький элемент во втором. Он добавляется в
# конце первого. Таким образом алгоритм постепенно формирует список от меньшего к большему.


def bubble_sort(ls):
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls




def selection_sort(ls):
    for i in range(len(ls)):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
        ls[i], ls[min_index] = ls[min_index], ls[i]
    return ls


def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while j >= 0 and key < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    return ls