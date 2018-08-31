build:
	python build.py

watch:
	find *.py *.tmpl* | entr make build

serve:
	python -m http.server 4001

dev-setup:
	pipenv install -d

deploy:
	netlifyctl deploy

ci: build

py-format:
	black *.py
