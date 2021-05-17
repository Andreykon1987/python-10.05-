duration = 153
seconds = duration % 60

if duration < 59:
    print(duration, 'сек')
elif duration >= 60 and duration <= 3599:
    minutes = duration // 60
    print(minutes, 'мин', seconds, 'сек')
elif duration >= 3600 and duration <= 86399:
    hours = duration // 3600
    duration = duration - (3600 * hours)
    minutes = duration // 60
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
elif duration >= 86400 and duration <= 604799:
    days = duration // 86400
    duration = duration - (86400 * days)
    hours = duration // 3600
    duration = duration - (3600 * hours)
    minutes = duration // 60
    print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')