import requests
import json
import concurrent.futures
from jsonschema import validate
from schemas.festivals_schema import festivals_schema


def test_get_festivals_status_response(festivals_endpoint):
  response =  requests.get(festivals_endpoint)
  assert response.status_code == 200
  assert response.headers["Content-Type"] == "application/json; charset=utf-8"

  resp_body = response.json()
  validate(instance=resp_body, schema=festivals_schema)


def test_delete_festivals(festivals_endpoint):
  response =  requests.delete(festivals_endpoint)
  assert response.status_code == 404


def test_get_festivals_throttled(festivals_endpoint):

  n = 10 # burst limit

  with concurrent.futures.ThreadPoolExecutor(max_workers=n+1) as executor:
    resps = executor.map(requests.get, [festivals_endpoint]*(n+1))

  resp_dict = {resp.status_code:resp for resp in resps}

  assert 429 in resp_dict.keys()
  assert resp_dict[429].text == "Too many requests, throttling"
