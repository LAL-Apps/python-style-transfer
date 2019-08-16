init:
	pip3 install -r requirements.txt

test:
	#Install the current package before running the test so pytest can use it like users
	pip3 install -e .
	pytest
