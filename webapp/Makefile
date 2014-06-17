# simple makefile to simplify repetetive build env management tasks under posix

NOSETESTS ?= nosetests3

all: clean test

test-code:
	$(NOSETESTS) -s -v webapp

test-coverage:
	rm -rf coverage .coverage
	$(NOSETESTS) -s -v --with-coverage webapp

test: test-code test-coverage
