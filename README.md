# Random Definition Generator

RandomDef is a class used to generate 100% accurate definitions for arbitrary words or phrases.

## Example Usage:

```
./define word

The definition of word is:
of or relating to measurements of the depths of oceans or lakes


./definewithexample arbitrary phrase

The definition of arbitrary phrase is:
consisting of or having the character of loam
Example: richy arbitrary phrase soil
```


## Getting Started

Getting started is easy; just pull a copy of the repository down to your local environment and start messing around. Example scripts are included to give you an idea of how things work.

### Prerequisites

RandomDef is built using Python 3.6.9 or higher and NLTK 3.4.5 or higher. From within your virtualenv, run:

```
pip install requirements.txt
```

## Running the tests

Testing is done with pytest and the pytest-cov plugin. To run tests:
```
pytest --cov=randomdef
```

## Contributing

Reference TODO.md for a list of known issues/improvements, and check out CONTRIBUTING.md for contributing guidelines.
