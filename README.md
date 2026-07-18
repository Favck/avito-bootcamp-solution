# 🚀 Инструкция по запуску проекта

## 0. Если у вас нет uv

Вы можете быстро установить его через обычный `pip`:
```bash
pip install uv
```

Либо запустите проект стандартными средствами Python (без `uv`):
```bash
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate.bat     # Windows (CMD)
pip install -r requirements.txt
python -m jupyter notebook
```

---

## 1. Установка окружения и зависимостей (через uv)

```bash
# 1. Создать виртуальное окружение
uv venv

# 2. Активировать окружение (выберите команду под вашу ОС):
source .venv/bin/activate      # Linux / macOS
.venv\Scripts\activate.bat     # Windows (CMD)
.venv\Scripts\Activate.ps1     # Windows (PowerShell)

# 3. Установить зависимости
uv pip install -r requirements.txt
```

## 2. Запуск исследования (Jupyter)

```bash
uv pip install jupyter
uv run jupyter notebook
```

**Работа в IDE (VS Code / PyCharm):**
Откройте ноутбук и выберите созданное ядро (Kernel) по пути:
* `../.venv/bin/python` (Linux/macOS)
* `..\.venv\Scripts\python.exe` (Windows)

## 3. Структура данных

Для работы пайплайна в корне проекта должны лежать файлы:
* `train.csv` и `test.csv` — статические таблицы.
* `events.csv` — сырые логи пользовательской активности.

Итоговый файл `submission.csv` генерируется автоматически в конце выполнения ноутбука.