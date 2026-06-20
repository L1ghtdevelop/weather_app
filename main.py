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
            os.system("clear||cls")
            print("="*50)
            user_input = input("Напишите название города, для которого хотите узнать погоду: ")
            user_data = controller.get_weather_data(user_input)
            os.system("clear||cls")
            print("="*50)
            text = controller.format_weather_data(user_data)
            if text:
                print(text)
            else:
                print("Вы неправильно ввели название города или такого города не существует")
            input(">>> ")
        
            
            
        elif choice == "2":
            history_manager.show_history()
            pass
            
        elif choice == "3":
            print("\n👋 До свидания!")
            break
            
        else:
            print("❌ Неверный выбор!")
            input("\n⏎ Нажмите Enter...")

if __name__ == "__main__":
    main()