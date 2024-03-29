import json
from pytest import mark, raises

def json_data():
  return {
  }

@mark.word
def test_(app, client):
  res = client.post('/', json=json_data())

  assert res.status_code == 200

  result = json.loads(res.get_data())
  assert isinstance(result, dict)

  assert result['code'] == 200
  assert result['status'] == 'success'

@mark.word
def test_add(app, client):
  res = client.post('/add', json=json_data())

  assert res.status_code == 200

  result = json.loads(res.get_data())
  assert isinstance(result, dict)

  assert result['code'] == 200
  assert result['status'] == 'success'