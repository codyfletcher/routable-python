import pytest

from routable import Client


class Test__Client__instantiation:
    def test_can_instantiate_Client_with_any_string_for_authentication_token(self):
        authentication_token = "FAKE_AUTHENTICATION_TOKEN"

        client = Client(authentication_token)

        assert client is not None


    def test_can_not_instantiate_Client_without_authentication_token__raises_TypeError(self):
        with pytest.raises(TypeError):
            _ = Client()

    def test_default_headers(self):
        client = Client("FAKE_AUTHENTICATION_TOKEN")

        expected_default_headers = {
            'Authorization': 'Bearer FAKE_AUTHENTICATION_TOKEN',
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }
        assert expected_default_headers == client.headers
