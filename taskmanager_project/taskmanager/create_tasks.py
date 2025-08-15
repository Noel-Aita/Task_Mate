# Import the requests library for making HTTP requests
import requests

# Define the endpoint for creating tasks
url = "http://127.0.0.1:8000/api/tasks/"

# Define the data for the new task (payload)
tasks = [
    {
        "title": "Install solar inverter",
        "description": "2KW backup system",
        "assigned_to": "Moses",
        "is_completed": False
    },
    {
        "title": "Repair faulty CCTV",
        "description": "Check DVR and cables",
        "assigned_to": "Lilian",
        "is_completed": False
    },
    {
        "title": "Upgrade lighting system",
        "description": "Replace bulbs with LEDs",
        "assigned_to": "Dennis",
        "is_completed": True
    }
]

for task in tasks:
    response = requests.post("http://127.0.0.1:8000/api/tasks/", json=task)
    print(f"Task: {task['title']} - Status: {response.status_code}")
    if response.status_code == 201:
        print("Created:", response.json())
    else:
        print("Error:", response.text)
