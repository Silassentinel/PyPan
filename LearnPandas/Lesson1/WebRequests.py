# cheatsheet for webrequests
import requests

#post

r = requests.post("https://httpbin.org/post", data = {'key':'value'})
print(r.text)

#get

r = requests.get("https://httpbin.org/get")
print(r.text)

#put

r = requests.put("https://httpbin.org/put", data = {'key':'value'})
print(r.text)

#delete

r = requests.delete("https://httpbin.org/delete")
print(r.text)

#patch

r = requests.patch("https://httpbin.org/patch", data = {'key':'value'})
print(r.text)
