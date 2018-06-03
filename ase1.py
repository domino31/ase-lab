import numpy as np
import time


l_elem = 10000
tab = []

def losowanie(tab):
    for i in range(l_elem):
        liczba = np.random.randint(1000000)
        if liczba not in tab:
            tab.append(liczba)

def babelkowy(tab):
    for i in range(dlugosc):
        j = dlugosc - 1
        while j > i:
            if tab[j] < tab[j - 1]:
                buf = tab[j]
                tab[j] = tab[j - 1]
                tab[j - 1] = buf
            j -= 1
    return tab


def wymiana(tab):
    for i in range(0, dlugosc-1):
        najmniejszy = min(tab[i:])
        # print(najmniejszy)
        gdzie = tab.index(najmniejszy)
        buf = tab[i]
        tab[i] = tab[gdzie]
        tab[gdzie] = buf
        # i+=1
    return tab


def pivot(tab, mniejszy, wiekszy):
    i = (mniejszy - 1)
    pivot = tab[wiekszy]

    for j in range(mniejszy, wiekszy):
        if tab[j] <= pivot:
            i = i + 1
            buf = tab[i]
            tab[i] = tab[j]
            tab[j] = buf

    buf = tab[i+1]
    tab[i+1] = tab[wiekszy]
    tab[wiekszy] = buf
    return (i + 1)


def quicksort(tab, mniejszy, wiekszy):
    if mniejszy < wiekszy:
        p = pivot(tab, mniejszy, wiekszy)

        quicksort(tab, mniejszy, p - 1)
        quicksort(tab, p + 1, wiekszy)


losowanie(tab)
print(tab)
babelkowy_tab = tab.copy()
wymiana_tab = tab.copy()
quicksort_tab = tab.copy()

dlugosc = len(tab)

print("bąbelkowy")
czas_start = time.time()
babelkowy(babelkowy_tab)
print(babelkowy_tab)
czas_stop = time.time()
print("czas trwania:", czas_stop - czas_start)

print('przez wymiane')
czas_start = time.time()
wymiana(wymiana_tab)
czas_stop = time.time()
print("czas trwania:", czas_stop - czas_start)
print(wymiana_tab)

print('quicksort')
czas_start = time.time()
# quicksort(quicksort_tab)
quicksort(quicksort_tab, 0, dlugosc-1)
czas_stop = time.time()
print("czas trwania:", czas_stop - czas_start)
print(quicksort_tab)
