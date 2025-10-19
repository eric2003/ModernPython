def get_users() -> dict[int, str]:
    users: dict[int, str] = {1: 'Bob', 2: 'Jef', 3:'Tom'}
    return users
    
def display_users(users: dict[int, str]) -> None:    
    for k, v in users.items():
        print(k, v, sep=': ')
        
def main() -> None:
    users: dict[int, str] = get_users()
    display_users(users)

if __name__ == '__main__':
    main()