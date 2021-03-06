# routable-python

This is a work-in-progress. I'm using this as an exercise to practice my craft, kick the tires on the [Routable API](https://developers.routable.com/docs), and get to know the domain/language in the [Routable universe](https://apidocs.routable.com/). 

How I've been working:

- Test-driving (TDD) the implementation of things. Attempting to _earn_ every line of code.
- Working in small increments ([DTSTTCPW](http://c2.com/xp/DoTheSimplestThingThatCouldPossiblyWork.html))
- Using [Arlo's Commit Notation](https://github.com/RefactoringCombos/ArlosCommitNotation) for commit messages
- Attempting to avoid [primitive obsession](https://wiki.c2.com/?PrimitiveObsession) by mirroring the domain (e.g. retrieve a list of `Membership` instead of `dict`)

## Getting Started

```python
from routable import Client

authentication_token = "XXXXXXXXXXXXX"
client = Client(authentication_token)

# Memberships
print("Here are the memberships in your account:")
memberships = client.memberships.list()
for m in memberships:
    print(m)

```

## Working in Development

Get a simple development environment created and activated:

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

### Python Tests (via `pytest`):

```shell
pytest .
```

### Static Type Checking (via `mypy`):

```shell
mypy .
```

### Code Metrics

Calculate cyclometic complexity (via `radon`):

```shell
# View cyclomatic complexity for all (F)unctions, (C)lasses, and (M)ethods
radon cc --show-complexity routable/

# View cyclomatic complexity that is below a score of "A" 
radon cc --show-complexity --min B routable/
```

Calculate Halstead Metrics (via `radon`):

```shell
# View on a per-file basis
radon hal routable/ 

# View on a per-function basis
radon hal --functions routable/
```

(EXPERIMENTAL) Calculate maintainability index (via `radon`):

```shell
# View cyclomatic complexity for all (F)unctions, (C)lasses, and (M)ethods
radon mi routable/
```

Calculate raw metrics (via `radon`):

```shell
# View metrics for each file (including summary)
radon raw --summary routable/

# View metrics for each file (including summary), excluding tests
radon raw --summary --exclude "**/tests/**" routable/
```



