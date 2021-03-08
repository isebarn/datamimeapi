

@mark.translations
def test_add(app, client):
  res = client.post('/add', json=json_data())

  assert res.status_code == 200

  result = json.loads(res.get_data())
  assert isinstance(result, dict)

  assert result['code'] == 200
  assert result['status'] == 'success'