def get_users() -> dict[int, str]:
    users: dict[int, str] = {1: 'Bob', 2: 'Jef', 3:'Tom'}
    return users
    
print(get_users())