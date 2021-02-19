def pref_func(S: str):
    """
    На основании префиксов и суфиксов строки
    находит максимальный префикс, который повторяется
    сложность - O(N)
    """
    pref = [0] * len(S)
    for i in range(1, len(S)):
        p = pref[i - 1]
        while p > 0 and S[i] != S[p]:
            p = pref[p-1]
        if S[i] == S[p]:
            p += 1
        pref[i] = p
    return pref.index(max(pref))


def substring(S, sub):
    """
    Алгоритм Кнута Морриса Пратта
    Сложность O(N + M)
    """
    return pref_func(sub + '#' + S) - 2 * len(sub)


def test(func):
    if substring('aabcdabcd', 'aab') == 0:
        print('Test 1 complete!')
    else:
        print('Test 1 fail')

    if substring('aabcdabcd', 'bcd') == 2:
        print('Test 2 complete!')
    else:
        print('Test 2 fail')

    if substring('aabcdabcd', 'dabcd') == 4:
        print('Test 3 complete!')
    else:
        print('Test 3 fail')


test(substring)
