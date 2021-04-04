import requests

BASE = "http://127.0.0.1:5000/"

prozess1 = r"\TestFlask\P1 (en).bpmn"
prozess2 = r"\TestFlask\P2 (en).bpmn"

response = requests.get(BASE + f"similarity/{prozess1}/{prozess2}")

print(response.json())



