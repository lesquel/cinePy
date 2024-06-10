import requests
def GetData(url):
    response = requests.get(f"http://localhost:8080/{url}")
    return response.json()
