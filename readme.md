## Шаблон DS проекта команды AI Дирекции B2B экосистемы

Рекомендуемый шаблон для нового проекта и сохранения проекта в BitBucket.

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
1. Python 3
1. Утилита [poetry](https://python-poetry.org/docs/#installation)
1. Утилита [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)

Сначала создаем директорию с проектом с помощью cookiecutter через http
```
cookiecutter git+https://stash.sigma.sbrf.ru/scm/b2b_ecosystem_ai/ds-project-template.git
```
или через ssh
```
cookiecutter git+ssh://git@stash.sigma.sbrf.ru:7999/b2b_ecosystem_ai/ds-project-template.git
```

Затем переходим в директорию с проектом
```
cd [directory_name]
```

Устанавливаем базовые пакеты (notebook, pandas, sklearn)
```
make install
```
и добавляем те, которые нужны для этого проекта
```
poetry add [package_name]
```

Запуск jupyter notebook
```
poetry jupyter notebook
```
