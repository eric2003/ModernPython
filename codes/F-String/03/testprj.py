from datetime import datetime
now: datetime = datetime.now()

print(f'{now:%d.%m.%y}')
