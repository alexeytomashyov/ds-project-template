import os
from pathlib import Path


basename = os.path.basename(Path.cwd().parent)

os.makedirs(f'/Volumes/EcosystemB2B/AI/data/{basename}/{{cookiecutter.directory_name}}', exist_ok=True)

makefile = f"""
install:
	poetry add --dev notebook
	poetry add --dev pandas
	poetry add --dev sklearn

get_data:
	cp -r /Volumes/EcosystemB2B/AI/data/{basename}/{{cookiecutter.directory_name}}/ ./data/

push_data:
	cp -r ./data/ /Volumes/EcosystemB2B/AI/data/{basename}/{{cookiecutter.directory_name}}/
"""

with open('Makefile', 'w') as file:
    file.write(makefile)
