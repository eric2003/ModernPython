from datetime import datetime
now: datetime = datetime.now()

print(f'{now:%d.%m.%y (%H:%M:%S)}')
print(f'{now:%c}')
print(f'{now:%I%p}')
