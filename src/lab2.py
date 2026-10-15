# Лабораторна робота №2. Створення та використання функцій, реалізація рекурсії
# Варіант: 2 (впишіть свій варіант)
# ПІБ: Зеленько Ярослав Олександрович (впишіть своє ПІБ)

# Тут має бути Ваш код
games = [
    {"name": "Minecraft", "hours": 50, "rating": 9.0},
    {"name": "GTA V", "hours": 40, "rating": 9.2},
    {"name": "The Witcher 3", "hours": 60, "rating": 9.5},
    {"name": "Cyberpunk 2077", "hours": 30, "rating": 8.5},
    {"name": "CS2", "hours": 100, "rating": 8.0},
    {"name": "Dota 2", "hours": 80, "rating": 8.2},
    {"name": "Fortnite", "hours": 25, "rating": 7.8},
    {"name": "Terraria", "hours": 20, "rating": 8.8},
    {"name": "Stardew Valley", "hours": 15, "rating": 8.7},
    {"name": "Elden Ring", "hours": 35, "rating": 9.4},
    {"name": "Portal 2", "hours": 10, "rating": 9.1},
    {"name": "Skyrim", "hours": 45, "rating": 9.3},
    {"name": "Fallout 4", "hours": 25, "rating": 8.4},
    {"name": "Among Us", "hours": 8, "rating": 7.5},
    {"name": "The Sims 4", "hours": 20, "rating": 7.9},
    {"name": "Forza Horizon 5", "hours": 30, "rating": 8.6},
    {"name": "God of War", "hours": 18, "rating": 9.2},
    {"name": "Red Dead Redemption 2", "hours": 55, "rating": 9.6},
    {"name": "Half-Life 2", "hours": 12, "rating": 9.0},
    {"name": "Dark Souls 3", "hours": 28, "rating": 8.9}
]


def show_games():
 # Показує всі ігри
    for game in games:
        print(game["name"], "-", game["hours"], "годин")


def add_hours(name, hours=1):
    # Додає години до гри
    for game in games:
        if game["name"].lower() == name.lower():
            game["hours"] += hours
            print("Години додано!")
            return
    print("Гру не знайдено.")


def total_hours(hours, index=0):
    # Рекурсивно рахує години
    if index == len(hours):
        return 0
    return hours[index] + total_hours(hours, index + 1)


def find_games(rating=8.5):
    # Знаходить ігри за рейтингом
    result = list(filter(lambda game: game["rating"] >= rating, games))
    for game in result:
        print(game["name"], "-", game["rating"])


def show_favorites(*names):
    # Показує обрані ігри
    for name in names:
        for game in games:
            if game["name"].lower() == name.lower():
                print(game["name"], "-", game["rating"])
                break
        else:
            print(name, "- не знайдено")


def process_data(function):
    # Обробляє список ігор заданою функцією
    return list(map(function, games))


def main():
    # Головне меню програми
    while True:
        print("\n1. Показати ігри\n2. Додати години")
        print("3. Порахувати всі години\n4. Пошук за рейтингом")
        print("5. Обрані ігри\n0. Вихід")
        choice = input("Ваш вибір: ")

        try:
            if choice == "1":
                show_games()
            elif choice == "2":
                name = input("Назва гри: ")
                hours = int(input("Години: "))
                if hours >= 0:
                    add_hours(name, hours)
                else:
                    print("Години не можуть бути від'ємними.")
            elif choice == "3":
                hours = process_data(lambda game: game["hours"])
                print("Усього годин:", total_hours(hours))
            elif choice == "4":
                rating = float(input("Мінімальний рейтинг (0-10): "))
                if 0 <= rating <= 10:
                    find_games(rating)
                else:
                    print("Рейтинг має бути від 0 до 10.")
            elif choice == "5":
                names = input("Назви ігор через кому: ").split(",")
                show_favorites(*[name.strip() for name in names])
            elif choice == "0":
                break
            else:
                print("Невірний пункт меню.")
        except ValueError:
            print("Помилка! Перевірте введені дані.")


if __name__ == "__main__":
    main()

# Не забувайте форматувати вивід та додавати коментарі!
