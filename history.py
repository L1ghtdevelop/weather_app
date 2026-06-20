import json

import os
from datetime import datetime

HISTORY_FILE = "history.json"

class HistoryManager:
    def load_history(self) -> list:
        if os.path.exists(HISTORY_FILE):
            if os.path.getsize(HISTORY_FILE) != 0:
                with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                    return json.load(f)
            else: 
                return []
        else: 
            return []

    def save_history(self, history: list) -> None:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4, ensure_ascii=False)

    def add_to_history(self, city: str, temperature: float) -> None:
        history: list = self.load_history()

        entry = {
            "city": city,
            "temperature": temperature,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        history.append(entry)
        if len(history) > 10:
            history = history[-10:]
        self.save_history(history)

    def show_history(self) -> None:
        history = self.load_history()

        if not history:
            print("История запросов пуста")
            return

        print("\n" + "="*50)
        print("📜 ИСТОРИЯ ЗАПРОСОВ (последние 10)")
        print("="*50)
        for i, entry in enumerate(reversed(history), 1):
            print(f"{i}. {entry['city']} | {entry['temperature']}°C | {entry['timestamp']}")
        print("="*50)