# List available commands
help:
    just --list

docs:
	cd docs && poetry run make html

clean:
	cd docs && poetry run make clean

# Post-installation tests
test:
	poetry run mypy src/lazychains/lazychains.py --check-untyped-defs
	poetry run pytest tests

# ATM I do not intend for updates of the PyPI archive to be run automagically.
# So these commands should be run locally before trying to update the PyPI
# archives.
# 	poetry config --local repositories.pypi https://pypi.org/legacy/
# 	poetry config --local pypi-token.pypi <your-token>
# 	poetry config --local repositories.test-pypi https://test.pypi.org/legacy/
# 	poetry config --local pypi-token.test-pypi <your-token>

publish:
	poetry publish --build

publish-to-test:
	poetry publish -r test-pypi --build
