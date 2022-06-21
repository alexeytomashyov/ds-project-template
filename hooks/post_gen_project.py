import os
from pathlib import Path


basename = os.path.basename(Path.cwd().parent)

os.makedirs(f'/Volumes/EcosystemB2B/AI/data/{basename}/{{cookiecutter.directory_name}}', mode=0o700, exist_ok=True)

makefile = f"""
install:
	poetry add --dev notebook
	poetry add --dev pandas
	poetry add --dev sklearn
    poetry add --dev matplotlib

get_data:
	cp -r /Volumes/EcosystemB2B/AI/data/{basename}/{{cookiecutter.directory_name}}/ ./data/

push_data:
	cp -r ./data/ /Volumes/EcosystemB2B/AI/data/{basename}/{{cookiecutter.directory_name}}/
"""

with open('Makefile', 'w') as file:
    file.write(makefile)

readme = f"""## 1. Описание
Кратко описать суть проекта. Можно дать ссылку на confluence.

Окружение устанавливается с помощью утилиты [poetry](https://python-poetry.org/docs/#installation) следующей командой
```
poetry install
```

## 2. data
Данные проекта лежат на сетевом диске EcosystemB2B в папке AI/data/{basename}/{{cookiecutter.directory_name}}/

Загрузить их можно с помощью команды
```
make get_data
```
N.B. Чтобы подключить сетевой диск на Mac нужно
- в **Finder** открыть меню *Переход/Подключение к Серверу...*
- ввести название сервера `smb://Rubin1.sigma.sbrf.ru/vol2/EcosystemB2B`
- нажать **Подключиться**

### raw

## 3. notebooks

## 4. docs
## 5. results
## 6. models
"""

with open('README.md', 'w') as file:
    file.write(readme)
