## Шаблон DS проекта

Рекомендуемый шаблон для нового проекта

### Структура директории
```bash
ds-project-template/
├── data/
│   ├── final/      # данные, полученные на выходе из модели
│   ├── processed/  # обработанные данные
│   └── raw/        # исходные данные до какой-либо обработки
├── docs/           # документы по проекту
├── models/         # модели
├── notebooks/      # jupyter ноутбуки
├── results/        # результаты, например, отчет о разработке модели
│                   # или презентация для заказчика
└── README.md       # описание проекта
```

### Порядок инициализации проекта
#### Пререквизиты
- Python 3
- Утилита [poetry](https://python-poetry.org/docs/#installation)
- Утилита [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)

1. Подключаем сетевой диск EcosystemB2B

1. Создаем директорию с проектом с помощью cookiecutter через http
```
$ cookiecutter git+https://github.com/alexeytomashyov/ds-project-template.git
```
или через ssh
```
$ cookiecutter git+ssh://git@github.com:alexeytomashyov/ds-project-template.git
```
2. Переходим в директорию с проектом
```
$ cd [directory_name]
```
3. Устанавливаем базовые пакеты (notebook, pandas, sklearn)
```
$ make install
```
и добавляем те, которые нужны для этого проекта
```
$ poetry add [package_name]
```
4. Запуск jupyter notebook
```
$ poetry run jupyter notebook
```
