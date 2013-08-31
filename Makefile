default: all

all:
	python setup.py build

install: all
	python setup.py install

clean:
	rm -f *.pyc
	cd tests && rm -f *.pyc
	cd cpu_cores && rm -f *.pyc
	cd tests && rm -Rf htmlcov 
	rm -Rf cpu_cores.egg-info
	rm -f .coverage tests/.coverage
	rm -f MANIFEST
	rm -Rf build
	rm -Rf dist
	rm -Rf cpu_cores.egg-info
	rm -Rf cpu_cores/__pycache__
	rm -Rf tests/__pycache__

sdist: clean
	python setup.py sdist

test:
	cd tests && nosetests

upload:
	python setup.py sdist register upload

coverage:
	cd tests && coverage run `which nosetests` && coverage html --include='*/cpu_cores/*' --omit='test_*'

release: test coverage clean upload clean 

flake8:
	find . -name "*.py" -exec flake8 {} \;
