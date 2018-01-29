# Requests 라이브러리 사용법
- GET, POST 등의 메서드의 사용
```python
# GET 요청
r = requests.get("http://google.com")

# POST 요청
formdata = { "key1": "value1", "key2": "value2" }
r = requests.post("http://example.com", data=formdata)
```

- 그 밖에 PUT/DELETE/HEAD 등의 요청을 위한 메서드
```python
# PUT
r = requests.put("http://httpbin.org/put")
# DELETE
r = requests.delete("http://httpbin.org/delete")
# HEAD
r = requests.head("http://httpbin.org/get")
```
GET, POST 등의 리턴값에 있는 text와 content 속성을 참조하여 내부의 데이터를 확인할 수 있다.