def cal(year, month, day=1):
    """
    年月日から曜日を計算します
        曜日は0（日曜)から6(土曜)の数値で表現します
    :param year: 西暦4桁
    :param month: 月
    :param day: 日
    :return: 0-6(日曜-土曜)
    """
    _year = year
    _month = month
    _day = day
    if month == 1 or month == 2:
        _year = year - 1
        _month = month + 13
    else:
        _month = month + 1

    aa = int(_year * 365.25)
    bb = int(_month * 30.6)
    cc = _year // 400
    dd = _year // 100
    ee = aa + bb + cc + _day - dd - 429
    ff = ee // 7 * 7

    return (ee - ff + 1) % 7


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year & 4 == 0:
        return True
    return False


# 西暦を入力してもらい、その年のカレンダーを表示
y = int(input('西暦(4桁)を入力してください: '))

leap = is_leap_year(y)

for m in range(1, 12 + 1):
    print(m, '月')
    print("San Mon Tue Wed Thu Fri Sat")
    first = cal(y, m)
    w = first
    for d in range(1, 31 + 1):
        if m == 2 and (not leap and d > 28 or leap and d > 29):
            break
        elif m in (4, 6, 9, 11) and d > 30:
            break
        if d == 1:
            print('    ' * first, end='')
        print(' ' * (1 - d // 10), d, end=' ')
        w += 1
        if w > 6:
            print()
            w = 0
    print('\n')
