## 📂 Структура проекта

Репозиторий имеет модульную структуру, разделяющую исследовательскую часть (Jupyter), продуктовый код (скрипты) и слои данных:

```text
AVITO_BOOTCAMP/
├── data/                   # Директория для исходных датасетов (train.csv, test.csv, events.csv)
├── notebooks/              
│   └── solution.ipynb      # Основной jupyter-ноутбук с решением
├── output/                 # Папка для результатов
│   └── .gitkeep            # Сюда сохраняется итоговый submission.csv
├── src/                    # Продуктовый код и переносимые модули
│   ├── evaluate.py         # Скрипт локальной валидации и расчета метрик (Daily AP)
    ├── features.py         # Работа с фичами
│   └── preprocessing.py    # Разбиение на train val
├── .gitignore             
├── .python-version        
├── pyproject.toml          
├── README.md              
└── uv.lock                 
```

## 🚀 Инструкция по запуску проекта

Проект инициализирован как полноценный **uv**-проект (использует `pyproject.toml` и `uv.lock`).

## 0. Если у вас нет uv

Самый быстрый способ запустить проект — поставить `uv` через обычный `pip`:
```bash
pip install uv
```

---

## 1. Установка окружения и зависимостей (Natively via uv)

Выполните в корне проекта:

```bash
uv sync
```

## 2. Запуск исследования (Jupyter)

```bash
uv run jupyter notebook
```

**Работа в IDE (VS Code / PyCharm):**
Откройте ноутбук решения и выберите созданный интерпретатор (Kernel) по пути:
* `../.venv/bin/python` (Linux/macOS)
* `..\.venv\Scripts\python.exe` (Windows)

## 3. Структура данных
Скачать данные https://disk.yandex.ru/d/Bkr7LdcAJdLvUA
Для работы пайплайна в корне проекта должны лежать файлы:
* `train.csv` и `test.csv` — статические таблицы.
* `events.csv` — сырые логи пользовательской активности.

Итоговый файл `submission.csv` сгенерируется автоматически в конце выполнения ноутбука.

