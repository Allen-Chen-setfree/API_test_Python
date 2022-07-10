# API testing with Python and Pytest

## Prerequisite
- Python >= '3.6'
- Install Pipenv (python -m pip install --user pipenv)

## Setup & Execute
- git clone https://github.com/Allen-Chen-setfree/API_test_Python.git
- cd API_test_Python
- python -m pipenv --python <exact_version_to_use: 3.8/3.9>
- python -m pipenv install
- python -m pipenv shell
- pytest src/API_tests.py --html=report.html

## Test Scenarios
- Status code 200 and Json response validation
- Status code 429 and String response validation
- Negative scenarios - Status 404
  - incorrect method
  - incorrect URL

## Next Step
- Security testing - ZAP
- Performance testing
