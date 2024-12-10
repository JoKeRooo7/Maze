PYTHON=python
VERSION=3.11
PY=$(PYTHON)$(VERSION)
PYSOURCE=.venv/bin/
DELETE_OUTPUT= > /dev/null
DIST_DIR=./output
DIR := $(CURDIR)/app
VENV_PY := .venv/bin/python
VENV_PIP := .venv/bin/pip

all: clean tests check_style install open

install: 
	@rm -rf ./$(DIST_DIR)
	@mkdir $(DIST_DIR)
	@$(VENV_PY) -m PyInstaller --name maze --onefile --distpath ./$(DIST_DIR) ./app/frontend/desktop_app/__main__.py

init_venv:
	@$(PY) -m venv .venv
	@$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r requirements.txt

uninit_venv:
	$(VENV_PIP) uninstall -r requirements.txt -y

open:
	$(DIST_DIR)/maze

uninstall: uninit_venv
	rm -rf $(DIST_DIR) build

dvi:
	@open ./README.html

dist:
	@mkdir archive_maze
	@cp -R output/maze archive_maze
	@tar cvzf archive_maze.tgz archive_maze
	@rm -rf archive_maze

tests: init_venv
	@export PYTHONPATH=$(DIR):$$PYTHONPATH && $(PYSOURCE)pytest -s -v  --durations=10 ../tests/*.py
	# deactivate

clean:
	@rm -rf $(DIST_DIR) ./.venv ./build ./*.spec ./*.tgz ./log ./archive_maze ./*.egg-info .pylintrc
	@find . -type d -name "__pycache__" -exec rm -rf {} +

check_style: init_venv
	$(PYSOURCE)yapf --recursive --style=google --diff $(shell find app -type f -name "*.py")
# $(PYSOURCE)autopep8 --max-line-length=80 --exit-code --aggressive --aggressive --diff $(shell find app -type f -name "*.py")
# $(PYSOURCE)black --check $(shell find app -type f -name "*.py")

format_style: init_venv
	$(PYSOURCE)yapf --in-place --recursive --style=google $(shell find app -type f -name "*.py")
# $(PYSOURCE)autopep8 --in-place --aggressive --aggressive $(shell find app -type f -name "*.py")
# $(PYSOURCE)black $(shell find app -type f -name "*.py")

build: install

rebuild: uninstall install

# upgrade_pip:
# 	$(PY) -m pip install --upgrade pip -q

# download_checking_style_module: upgrade_pip
# 	$(PY) -m pip install pylint -q

# download_formatting_style_module: upgrade_pip
# 	$(PY) -m pip install yapf -q
