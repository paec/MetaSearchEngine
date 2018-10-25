import requests
import json
# data = '{"username":"markchang", "passwd":"12345"}'
data = ' {"maps": [{"id": "字串","iscategorical": "0"},{"id": "blabla","iscategorical": "0"}] , "map2":"hello"} '

r = requests.post('http://127.0.0.1:5000/index',data.encode('utf-8'))


print(type(r.text))
print(r.text)

a = json.loads(r.text)

print(type(a))
dictkey = a.keys()
for k in dictkey:
	print(k)