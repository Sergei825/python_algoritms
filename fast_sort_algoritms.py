# Сортировки слиянием и Тони Хоара

def merge(A: list, B: list):
    """
    Объединение двух массивов в один.
    Нужен для сортировки слиянием.
    Для ускорения лучше передавать один
    массив с индексам разделения в нем.
    """
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
        else:
            C[n] = B[k]
            k += 1
        n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def merge_sort(A):
    """
    Сортировка слиянием.
    Сортирует переданный массив.
    Ничего не возвращает.
    Скорость = N*log(N)
    """
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = A[0:middle]
    R = A[middle:]
    merge_sort(L)
    merge_sort(R)
    # A = merge(L, R) ссылка переопределится
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]


def hoar_sort(A):
    """
    Сортировка Хоара.
    Сортирует массив. Скорость
    между N^2 и N*log(N)
    """
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x > barrier:
            R.append(x)
        else:
            M.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1


def test_sort(s_func):
    utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)
    print(s_func.__doc__, file=utf8stdout)
    A = [4, 2, 1, 3]
    s_func(A)
    if A == [1, 2, 3, 4]:
        print('OK')
    else:
        print('Fail')


test_sort(merge_sort)
test_sort(hoar_sort)
