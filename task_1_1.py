duration = int(input())
if duration < 60 :
    print(duration, 'сек')
elif duration < 60**2:
    m = duration // 60
    s = duration % 60
    print(f'{m} мин {s} сек')
elif duration < 60**2*24:
    h = duration // 60**2
    m = (duration - h*60**2) // 60
    s = duration % 60
    print(f'{h} час {m} мин {s} сек')
else:
    d = duration // 86400
    h = (duration - d*(60**2)*24) // 60 ** 2
    m = (duration - d*60**2*24 - h*60**2) // 60
    s = duration % 60
    print(f'{d} дн {h} час {m} мин {s} сек')

