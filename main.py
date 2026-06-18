import os
from api_client import get_weather_data, format_weather_data
from history import add_to_history, show_history

def main():
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
            # TODO: реализуйте запрос города и вывод погоды
            pass
            
        elif choice == "2":
            # TODO: показать историю
            pass
            
        elif choice == "3":
            print("\n👋 До свидания!")
            break
            
        else:
            print("❌ Неверный выбор!")
            input("\n⏎ Нажмите Enter...")

if __name__ == "__main__":
    main()