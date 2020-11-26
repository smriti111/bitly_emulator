import requests
username = 'pssmriti'
password = 'Smriti@123'

auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))

if auth_res.status_code == 200:
    print(auth_res.content.decode())
    #f4de0feb2477fef7db40a29a401fb5364089c9b1
    print()