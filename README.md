[![Python application test with Github Actions](https://github.com/noahgift/debugging-python/actions/workflows/blank.yml/badge.svg)](https://github.com/noahgift/debugging-python/actions/workflows/blank.yml)


# debugging-python
Obvious and non-obvious solutions for debugging Python Code


## Setup Virtualenv

A good way to debug code:  `virtualenv ~/.debug` `source ~/.debug/bin/activate`

## Continuous Integration (It isn't automated it is broken)

It seems like automated testing and linting is more work, but it is less.  You can even skip the testing and only lint your code.

* Setup python scaffold: `Makefile`, `app.py`, `requirements.txt` and `test_app.py`
* Test your code using `make lint` or `make test`.
* Test automatically with Github Actions

## Add print or logging statements

Print everything until you figure out what is going on

## Pull out the debugger.

`import pdb;pdb.set_trace()`

Can also use `ipdb`:  https://pypi.org/project/ipdb/

## Install IPython and import portions of your code and test it out

`from hello import add`


## Test your way out of the problem

Does anything work!!!  Write a test for something, anything and see if it works.


