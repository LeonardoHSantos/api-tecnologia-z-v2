import requests
from plataform import urls_iqoption

from .prepare_message import prepare_response

def auth_user(identifier, password):
    data = {
        "identifier": identifier,
        "password": password,
    }
    r = prepare_response(requests.post(url=urls_iqoption.URL_HTTP, data=data).content)
    if r["code"] == "success":
        urls_iqoption.SSID = r["ssid"]
        return [200, urls_iqoption.SSID]
    return [401, "credencias inválidas"]