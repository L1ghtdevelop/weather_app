import os

from api_client import ControllerAPI
from history import HistoryManager

def main():
    history_manager = HistoryManager()
    
    controller = ControllerAPI()
    while True:
        os.system("clear||cls")
        print("\n" + "="*50)
        print("🌤️  ПОГОДНЫЙ АГРЕГАТОР")
        print("="*50)
        print("1. 🔍 Узнать погоду в городе")
        print("2. 📜 История запросов")
        print("3. 🚪 Выход")
        print("="*50)
        
        choice = input(">>> Выберите действие: ").strip()
        
        if choice == "1":
            history: list = history_manager.load_history()
            os.system("clear||cls")
            print("="*50)
            user_input = input("Напишите название города, для которого хотите узнать погоду: ")
            user_data = controller.get_weather_data(user_input)
            if user_data:
                history_manager.add_to_history(user_data["name"], user_data["main"]["temp"])
                os.system("clear||cls")
                print("="*50)
                text = controller.format_weather_data(user_data)
                if text:
                    print(text)
                else:
                    print("Вы неправильно ввели название города или такого города не существует")
            else:
                print("Город не найден или произошла ошибка...")
            input(">>> ")
        
        elif choice == "2":
            os.system("clear||cls")
            history_manager.show_history()
            input(">>> ")
            pass
            
        elif choice == "3":
            print("\n👋 До свидания!")
            break
            
        else:
            print("❌ Неверный выбор!")
            input("\n⏎ Нажмите Enter...")

if __name__ == "__main__":
    main()