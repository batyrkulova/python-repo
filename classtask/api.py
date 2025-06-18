import requests
import pprint

url = "https://backend.akumotechnology.com/api/users/me"
cookies = {"access_token_cookie": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlbHN1YmVrdGVtaXJvdmFAZ21haWwuY29tIiwiZXhwIjoxNzUwMTI2NjkyfQ.YTK4mrt7h3Htqp9I9cdZJ_qd3ndN3qwJ2j0IvWCfgSk"}
about_me = requests.get(url, cookies=cookies)

print((about_me.json()))