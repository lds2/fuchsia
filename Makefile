.PHONY: clean dist test

dist:
	sage -python setup.py sdist

register:
	sage -python setup.py register

upload-pypi:
	sage -python setup.py sdist upload

upload-http:
	@echo "Not implemented"

clean:
	@rm -fr build dist fuchsia.egg-info
	@rm -fr *.pyc */*.pyc

test:
	sage -python setup.py test

quicktest:
	env SAGE_PATH="$(CURDIR)" \
		sage -python -munittest -fv test.fast_test_suite

fuchsia.py: test/__init__.py

test/*.py::
	env SAGE_PATH="$(CURDIR)" \
		sage -python -munittest -fv test.$(basename $(notdir $@))
