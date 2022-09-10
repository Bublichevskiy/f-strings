import datetime

now = datetime.datetime.now()

print(now)
print(f'Сегодня {now:%d} {now:%8} {now:%Y}')
print(f'{now:%H} {now:%m} {now:%S}')