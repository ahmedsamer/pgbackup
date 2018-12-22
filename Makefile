.PHONNY: lint test install

default: test

lint: 
	flake8 --statistics

test: 
	PYTHONPATH=./src pytest -v

install: 
	pipenv install --dev --skip-lock
