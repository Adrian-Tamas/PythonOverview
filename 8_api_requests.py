import json
import requests
import httpx

from pprint import pprint as pp

BASE_URL = "https://httpbin.org"


payload = {
    "name": "Adrian",
    "id": 3,
    "email": "adrian@email.com"
}


def requests_get():
    response = requests.get(f"{BASE_URL}/get", params={"id": 3})
    return response.json()


def requests_post():
    response = requests.post(f"{BASE_URL}/post", json=payload)
    return response.status_code, response.content


def httpx_get():
    response = httpx.get(f"{BASE_URL}/get", params={"id": 3})
    return response.json()


def httpx_post():
    response = httpx.post(f"{BASE_URL}/post", json=payload)
    return response.status_code, response.content


def httpx_info():
    response = httpx.options(f"{BASE_URL}/status/200")
    return response.status_code, response.headers.multi_items()


if __name__ == '__main__':
    print("\nGet methods: \n")
    print("Response from requests", requests_get())
    print("Response from httpx", httpx_get())

    print("\nPost methods: \n")
    status_code, response = requests_post()
    print(f"Post request status code was {status_code} \n and the response was {response}")
    print(f"The json format of the response is: \n {json.loads(response)}")
    status_code, response = httpx_post()
    print(f"Post httpx status code was {status_code} \n and the response was {response}")
    print(f"The json format of the response is: \n ")
    pp(json.loads(response))

    print("\n Info method \n")
    status_code, headers = httpx_info()
    print(f"Info httpx status code was {status_code} \n and the headers was {headers}")
    print(f"The json format of the headers is: \n")
    pp(headers)
