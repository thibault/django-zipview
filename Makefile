test:
	flake8 zipview --ignore=E501
	coverage run --branch --source=zipview `which django-admin.py` test --settings=zipview.test_settings zipview
	coverage report --omit=zipview/test*

.PHONY: test
