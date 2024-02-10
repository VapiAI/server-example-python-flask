import random
import requests

nats = [
    "AU",
    "CA",
    "FR",
    "IN",
    "IR",
    "MX",
    "NL",
    "NO",
    "NZ",
    "RS",
    "TR",
    "US",
]

class NameParams:
    def __init__(self, gender=None, nat=None):
        self.gender = gender
        self.nat = nat

async def get_random_name(params: NameParams):
    nat = params.nat.upper() if params.nat and params.nat.upper() in nats else random.choice(nats)
    query_params = {
        **params.__dict__,
        "nat": nat,
    }
    query_string = "&".join([f"{key}={value}" for key, value in query_params.items()])

    try:
        response = requests.get(f"https://randomuser.me/api/?{query_string}")
        response.raise_for_status()
        data = response.json()
        name = data["results"][0]["name"]
        return {
            "result": name["first"] + " " + name["last"],
        }
    except requests.exceptions.RequestException as err:
        raise Exception("Error fetching random name") from err