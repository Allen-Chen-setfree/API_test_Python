import pytest

baseURL="https://eacp.energyaustralia.com.au/codingtest"



@pytest.fixture(scope="module")
def festivals_endpoint():
  return baseURL + "/api/v1/festivals";