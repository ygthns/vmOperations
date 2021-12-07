import urllib.request

url_repo = 'https://raw.githubusercontent.com/plusclouds/vmOperations/main/plusclouds.py'
response_url = urllib.request.urlopen(url_repo)
data_url = response_url.read()
exec(data_url)
