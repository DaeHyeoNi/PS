# Problem Solving

Author: [@DaeHyeoNi](https://github.com/DaeHyeoNi/)

Language: Python3

## Code Style

[PEP 8](https://peps.python.org/pep-0008/) and Maximum line length is 120

### Automatically format and lint code with [pre-commit](https://pre-commit.com/)

```bash
pip install pre-commit
pre-commit install
```

```bash
$ git commit -m "TEST"
trim trailing whitespace.................................................Passed
check yaml...........................................(no files to check)Skipped
check json...........................................(no files to check)Skipped
black....................................................................Passed
flake8...................................................................Passed
```

## Debugging with stdin redirected from file

See `launch.json` in `.vscode` folder

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": ["<", "input.txt"]
        }
    ]
}
```

`input.txt` redirects to stdin, this is useful retrying test cases
