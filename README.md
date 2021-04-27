## Examples

### Basic Usage

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
