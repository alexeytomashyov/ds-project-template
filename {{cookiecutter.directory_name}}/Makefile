install:
	poetry add --dev notebook
	poetry add --dev pandas
	poetry add --dev sklearn

get data:
	cp /Volumes/EcosystemB2B/AI/data/{{basename $(pwd)}}/{{cookiecutter.directory_name}}

push data:
	cp -r data /Volumes/EcosystemB2B/AI/data/{{basename $(pwd)}}/{{cookiecutter.directory_name}}
