import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout

# Адрес эндпоинта (порт мы уже проверили через netstat — 11434)
url = "http://localhost:11434/api/generate"

# Тело запроса (payload) — заполни сам
payload = {
    "model": "qwen3",
    "prompt": "Привет! Расскажи в двух предложениях, что ты умеешь делать для разработчика на Python?",
    "stream": False
}

try:
    # Отправка POST-запроса
    response = requests.post(url, json=payload, timeout=10)

    # Если сервер вернул ошибку (4xx/5xx), это вызовет исключение
    response.raise_for_status()

    # Разбор JSON-ответа
    data = response.json()

    # В ответе от /api/generate текст находится в поле "response"
    print("Ответ модели:")
    print(data["response"])

except ConnectionError:
    print("Ошибка соединения: сервер Ollama не найден.")
    print("Проверь: запущен ли Ollama (ollama version) и слушает ли порт 11434 (netstat).")
except HTTPError as e:
    print(f"HTTP-ошибка: {e}")
    print("Возможно, модель не найдена или неверный запрос.")
except Timeout:
    print("Превышено время ожидания ответа от модели.")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
