
Scrapy Parser для PEP документов
Описание проекта

Проект представляет собой парсер документов PEP (Python Enhancement Proposal) с использованием фреймворка Scrapy. Парсер собирает информацию о документах и сохраняет её в CSV-формате.
Установка и настройка

    Клонирование репозитория:

git clone https://github.com/vysochenkodanil/scrapy_parser_pep.git
cd scrapy_parser_pep

    Создание виртуального окружения:

python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate

    Установка зависимостей:

pip install -r requirements.txt

Запуск парсера

    Запуск паука:

scrapy crawl pep

    Параметры запуска:

    --output: указать путь для сохранения результатов

    --format: формат вывода (по умолчанию CSV)

Структура проекта

scrapy_parser_pep/
├── pep_parse/
│   ├── __init__.py
│   ├── settings.py
│   ├── pipelines.py
│   ├── utils.py
│   └── spiders/
│       └── pep_spider.py
├── tests/
│   ├── test_*.py
│   └── _tmp/
├── requirements.txt
└── README.md

Основные компоненты

    Spiders — содержит логику парсинга

    Pipelines — обработка и сохранение данных

    Settings — конфигурация проекта

    Tests — набор тестов для проверки работы

Результаты работы

После выполнения парсинга в директории results будут созданы следующие файлы:

    CSV-файл с основными данными PEP документов

    Файл с статистикой по статусам документов

Тестирование

Для запуска тестов выполните:

pytest

Требования

    Python 3.8+

    Scrapy

    LXML

    PyTest

    Другие зависимости из requirements.txt
    автор Высоченко Д.Л.