import json
import sys
from typing import Any


def calculate_cost(data: dict[str, Any]):
    message: str = data["extra"]["message"]
    return (message, int(message.split()[-1]))


def analyze(file_path):
    with open(file_path) as file:
        cost = 0
        message = ""
        data = json.load(file)
        data = data["results"]

        for el in data:
            val: tuple[str, int] = calculate_cost(el)
            message += val[0] + "\n"
            cost += val[1]

        print("Your cost is :", cost)

        if cost <= 500:
            print("Code is optimal")
        elif cost <= 1000:
            print("Code is semi optimal")
        else:
            print("Code is not optimal")

        print(message)


if __name__ == "__main__":
    json_file_path = sys.argv[1]
    analyze(json_file_path)
