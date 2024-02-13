import json
from pydantic import BaseModel
import httpx

BASE_URL = "https://httpbin.org"


class User(BaseModel):
    name: str
    id: int
    email: str

    @classmethod
    def create(cls, name: str,id: int):
        email = f"{name.lower()}@email.com"
        return cls(name=name, id=id, email=email)


def httpx_post():
    user = User.create(name="Adrian", id=3)
    print("user object: \n", user)
    print("user payload: \n", user.dict())
    response = httpx.post(f"{BASE_URL}/post", json=user.dict(), headers={"my_value": "1"})
    return response.status_code, response.content


if __name__ == '__main__':
    status_code, response = httpx_post()
    print(f"Post httpx status code was {status_code} \n and the response was {response}")
    print(f"The json format of the response is: \n {json.loads(response)}")
