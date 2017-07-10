import urllib, json

url=urllib.urlopen('http://httpbin.org/get')
text=url.read()

response=json.loads(str(text))

print response["origin"]

