import pytest
import requests


@pytest.mark.skip
@pytest.mark.functional
def test__no_authentication_credentials__gives_unauthorized_error__using_requests():
    url = "https://api.sandbox.routable.com/memberships/"

    payload = {}
    headers = {
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json'
    }

    response = requests.get(url, headers=headers, data=payload)

    print(response.text)

    expected_response = {
        'errors': {
            'unauthorized': {'detail': 'Authentication credentials were not provided.'
                             }
        }
    }
    assert expected_response == response.json()
