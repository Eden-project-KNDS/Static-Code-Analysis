import json
from typing import Any


def calculate_cost(data: dict[str, Any]) -> int:
    message: str = data["extra"]["message"]
    return int(message.split()[-1])


with open("semgrep_results.json") as file:
    cost = 0

    data = json.load(file)
    data = data["results"]

    for el in data:
        cost += calculate_cost(el)

    print("Your cost is :", cost)

    if cost <= 500:
        print("Code is optimal")
    elif cost <= 1000:
        print("Code is semi optimal")
    else:
        print("Code is not optimal")
