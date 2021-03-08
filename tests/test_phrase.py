import json
from pytest import mark, raises

def json_data():
  return {
  }

@mark.phrase
def test_list(app, client):
  res = client.post('/list', json=json_data())

  assert res.status_code == 200

  result = json.loads(res.get_data())
  assert isinstance(result, dict)

  assert result['code'] == 200
  assert result['status'] == 'success'