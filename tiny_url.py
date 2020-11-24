import requests
username='pssmriti'
password='Smriti@123'

#get access token
auth_res=requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password)))

#if status is ok
if auth_res.status_code==200:
    access_token=auth_res.content.decode()
    print("[!] Recieved the access token", access_token)
else:
    print("[!] Error while getting the access token")
    exit()



#construct the request header with authorization
headers = {"Authorization": f"Bearer {access_token}"}

#get the Group UID associated with your bitly account

group_res=requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)

if group_res.status_code==200:
    groups_data=group_res.json()['groups'][0]
    guid=groups_data['guid']

else:
    print("[!] cannot fetch the GUID exiting ....")
    exit()


#url u wanna shorten
url = "https://www.thepythoncode.com/topic/using-apis-in-python"

#post request to get the shortened url from api

shorten_res=requests.post()