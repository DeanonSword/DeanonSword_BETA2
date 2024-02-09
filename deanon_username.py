import json

def search_user_info(user_id):
    with open('user_data.json', 'r') as file:
        data = json.load(file)
        if user_id in data:
            print(f"Информация о пользователе с айди {user_id}:")
            print(json.dumps(data[user_id], indent=4))  # Вывод информации о пользователе в терминале
        else:
            print(f"Пользователь с айди {user_id} не найден.")

# Пример использования
user_id = input("Введите айди пользователя: ")
search_user_info(user_id)