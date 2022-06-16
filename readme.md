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
- Python 3
- Утилита [poetry](https://python-poetry.org/docs/#installation)
- Утилита [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)

1. Создаем директорию с проектом с помощью cookiecutter через http
```
cookiecutter git+https://stash.sigma.sbrf.ru/scm/b2b_ecosystem_ai/ds-project-template.git
```
или через ssh
```
cookiecutter git+ssh://git@stash.sigma.sbrf.ru:7999/b2b_ecosystem_ai/ds-project-template.git
```
2. Переходим в директорию с проектом
```
cd [directory_name]
```
3. Устанавливаем базовые пакеты (notebook, pandas, sklearn)
```
make install
```
и добавляем те, которые нужны для этого проекта
```
poetry add [package_name]
```
4. Запуск jupyter notebook
```
poetry jupyter notebook
```

### Загрузка проекта на Bitbucket
1. Создать новый репозиторий на Bitbucket с указанием КЭС. Например, `ast/complaints`
2. Привязать репозиторий к проекту
```bash
git init
git add --all
git commit -m "Initial Commit"
git remote add origin ssh://git@stash.sigma.sbrf.ru:7999/b2b_ecosystem_ai/{название репозитория}.git
git push -u origin
```
3. Сохранить данные на командном ФИРе
```
make push_data
```
N.B. Чтобы подключить сетевой диск на Mac нужно
- в finder открыть меню *Переход/Подключение к Серверу...*
- ввести название сервера `smb://Rubin1.sigma.sbrf.ru/vol2/EcosystemB2B`
- нажать **Подключиться**
