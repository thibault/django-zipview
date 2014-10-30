testenv:
	pip install -e .
	pip install -r requirements/test.txt
	pip install Django

test:
	flake8 zipview --ignore=E501
	coverage run --branch --source=zipview `which django-admin.py` test --settings=zipview.test_settings zipview
	coverage report --omit=zipview/test*

.PHONY: test
