import urllib3, json
url = "http://api.tvmaze.com/shows?page=1"
response = urllib3.HTTPConnectionPool.urlopen(url)
data = json.loads(response.read())
print(data)
#print(data[220]['name'])