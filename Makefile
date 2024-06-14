run:
	python src/main.py

install:
	pip install -r requirements.txt

mac:
	@echo "Gerando executável para macOS..."
	@cd src/scripts && ./mac_build.sh
	@echo "Executável para macOS gerado com sucesso!"

windows:
	@echo "Gerando executável para Windows..."
	@cd src/scripts && ./windows_build.bat
	@echo "Executável para Windows gerado com sucesso!"

.PHONY: install run mac windows
