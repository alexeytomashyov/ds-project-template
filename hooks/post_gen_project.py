import os
from pathlib import Path


os.remove('./data/.gitkeep')

makefile = f"""install:
	poetry add --dev notebook
	poetry add --dev pandas
	poetry add --dev sklearn
    poetry add --dev matplotlib

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
### raw

## 3. notebooks

## 4. docs
## 5. results
## 6. models
"""

with open('README.md', 'w') as file:
    file.write(readme)
