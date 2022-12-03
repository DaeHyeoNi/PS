# Problem Solving

Author: [@DaeHyeoNi](https://github.com/DaeHyeoNi/) <br />
Language: Python3

## Code Style
[PEP 8](https://peps.python.org/pep-0008/) and Maximum line length is 120

### Automatically format and lint code with [pre-commit](https://pre-commit.com/)
Q: Why use it?
A: pre-commit hook scripts are useful for identifying simple problems before pushing code.

```
$ pip install pre-commit
$ pre-commit install
```

```
$ git commit -m "TEST"
trim trailing whitespace.................................................Passed
check yaml...........................................(no files to check)Skipped
check json...........................................(no files to check)Skipped
black....................................................................Passed
flake8...................................................................Passed
```