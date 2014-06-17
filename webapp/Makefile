# simple makefile to simplify repetetive build env management tasks under posix

NOSETESTS ?= nosetests3

all: clean test

test-code:
	$(NOSETESTS) -s -v model

test-coverage:
	rm -rf coverage .coverage
	$(NOSETESTS) -s -v --with-coverage model

test: test-code test-coverage
