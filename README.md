# My Ollama Agent (Learning Project)

Простейший агент на Python, который взаимодействует с локальной LLM (модель Qwen3) через Ollama.

**Цель проекта:** показать два подхода к работе с API — через готовую библиотеку и через прямой HTTP‑запрос.

## Особенности проекта

- `agent_simple.py` — быстрый вариант через официальную библиотеку `ollama`.
- `agent_raw_http.py` — ручной HTTP‑запрос через `requests`, обработка ошибок и парсинг JSON. Это показывает понимание работы API «под капотом».
- Локальная работа: не нужны API‑ключи, всё крутится на твоём ПК.
- Воспроизводимость: зависимости в `requirements.txt`, запуск описан в этом README.

## Требования

- Python 3.14+
- Ollama (версия 0.40.2+)
- Модель `qwen3` (~5.2 ГБ)
- ОС: Windows / macOS / Linux

## Как запустить

1. Создай виртуальное окружение:
   ```bash
    python -m venv venv
2. Активируй его:
    ```bash
    Windows: venv\Scripts\activate
    macOS/Linux: source venv/bin/activate
3. Установи зависимости:
   ```bash
    pip install -r requirements.txt
4. Проверь, что Ollama запущен:
    ```bash
    ollama version
    ollama pull qwen3
5. Запусти нужный скрипт:
    ```bash
    python agent_simple.py или python agent_raw_http.py
## Структура проекта
    
```text
    my-ollama-agent/
    ├── agent_simple.py      # Вариант через библиотеку ollama
    ├── agent_raw_http.py    # Вариант через requests (raw HTTP)
    ├── requirements.txt     # Зависимости
    └── README.md            # Эта документация


