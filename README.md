# routable-python

This is a work-in-progress.

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

Get a simple development environment created and activated.

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

Run the tests:

```shell
pytest .
```

Run mypy

```shell
mypy .
```