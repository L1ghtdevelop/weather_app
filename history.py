import json

import os
from datetime import datetime

HISTORY_FILE = "history.json"

def load_history() -> list:
    return [] # TODO: Сделать загрузчик истории

def save_history(history: list) -> None:
    pass # TODO: Сделать сохранение истории

def add_to_history(city: str, temperature: float) -> None:
    history: list = load_history()

    entry = {
        "city": city,
        "temperature": temperature,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    history.append(entry)
    if len(history) > 10:
        history = history[-10:]
    save_history(history)
    
def show_history() -> None:
    history = load_history()

    if not history:
        print("История запросов пуста")
        return
    
    print("\n" + "="*50)
    print("📜 ИСТОРИЯ ЗАПРОСОВ (последние 10)")
    print("="*50)
    for i, entry in enumerate(reversed(history), 1):
        print(f"{i}. {entry['city']} | {entry['temperature']}°C | {entry['timestamp']}")
    print("="*50)