import requests
url = "https://api.track.toggl.com/api/v8/time_entries/start"
info = {"time_entry":{"description":"当前日期","tags":["内务"],"pid":164219861,"created_with":"curl"}}
headers = { 'Content-Type':  'application/json'}
response = requests.post(url,data=json.dump(info),headers=headers,auth=('873610008@qq.com','xgkLIJIN@369')) 
print(response.content)