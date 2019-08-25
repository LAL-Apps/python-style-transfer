init:
	pip3 install -r requirements.txt

test:
	#Install the current package before running the test so pytest can use it like users
	pip3 install -e .
	#Run pytest with live logging and debug level
	pytest -o log_cli=true --log-cli-level=DEBUG

publish:
	rm dist/*
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
