# simple makefile to simplify repetetive build env management tasks under posix

PYTHON3 ?= python3
NOSETESTS ?= nosetests3

all: clean test

test-django:
	$(PYTHON3) manage.py test

test-code: test-django
	$(NOSETESTS) -s -v webapp/recommend

test-coverage:
	rm -rf coverage .coverage
	$(NOSETESTS) -s -v --with-coverage webapp

test: test-code test-coverage
