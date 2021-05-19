import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYyMTM2MzA1OX0.Xcc6TKjnh5WDWmKIf4CQVQtdqT4NlIq1kXKzvhx1plc"

headers = {"Authorization": "Bearer {}".format(token)}


response = requests.get(
    "http://localhost:8000/posts",
    headers=headers,
)

print(response.json())
