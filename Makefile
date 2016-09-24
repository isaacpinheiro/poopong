.PHONY: clean clean-test test run

clean:
	rm -r src/__pycache__

clean-test:
	make clean
	rm -r test/__pycache__

test:
	python -m test.tests

run:
	python -m src.main
