language: python
python:
  - "2.7"
  - "3.3"
  - "3.4"
  - "3.5"
  - "3.6"
  - "nightly"
# command to install dependencies
install:
  - "pip install -r requirements.txt"
# command to run tests
script: pytest
