BASE = '/api/tasks/1/comments'

def test_create_comment(client):
    payload = {'author': 'Alice', 'content': 'Hello world'}
    res = client.post(BASE, json=payload)
    assert res.status_code == 201

def test_list_comments(client):
    client.post(BASE, json={'author':'A','content':'first'})
    client.post(BASE, json={'author':'B','content':'second'})
    res = client.get(BASE)
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)

def test_get_update_delete(client):
    res = client.post(BASE, json={'author':'X','content':'temp'})
    cid = res.get_json()['id']
    res = client.get(f'{BASE}/{cid}')
    assert res.status_code == 200
    res = client.put(f'{BASE}/{cid}', json={'author':'Y','content':'updated'})
    assert res.status_code == 200
    res = client.delete(f'{BASE}/{cid}')
    assert res.status_code == 204
