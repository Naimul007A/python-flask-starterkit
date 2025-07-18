copyenv:
	cp .env.example .env

run:
	python main.py

run-dev:
	FLASK_APP=main.py flask run --host=0.0.0.0 --port=8000 --debug

install:
	uv pip install -r requirements.txt

setup:
	make copyenv
	make install
