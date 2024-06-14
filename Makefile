run:
	python3.9 src/main.py

install:
	pip3.11 install -r requirements.txt

.PHONY: install run
