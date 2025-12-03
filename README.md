## Описание
Приложение для генерации отчетов по csv файлам

## Добавление новых отчетов
Для добавления нового отчета создать класс, реализующий интерфейс `IReport`

## Запуск
1. Установить зависимости
```bash
pip install -r requirements.py
```
2. Запустить скрипт
```bash
python -m app.main --files app/employees1.csv app/employees2.csv --report performance
```
<img width="1292" height="302" alt="Снимок экрана 2025-12-03 133947" src="https://github.com/user-attachments/assets/feee4b56-0c98-4b0e-9ebf-e5e7a7cfb29c" />


## Требования
- `pytest==9.0.1`
- `pytest-cov==7.0.0`
- `tabulate==0.9.0`
