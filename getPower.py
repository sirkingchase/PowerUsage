import os
import ssl
import requests
from urllib.parse import urlencode
from datetime import datetime, timedelta

def getPowerUsage(start, end):
    fileName = "pu_" + start.strftime("%Y%m%d") + "-" + end.strftime("%Y%m%d") + ".csv"
    print(fileName)
    p='https://myinfo.nbutexas.com:443/CC/connect/users/home/indicators/ExportExcelReadData.xml' \
    + '&StartDateTime=' + start.strftime('%Y-%m-%dT00:00:00') \
    + '&EndDateTime=' + end.strftime('%Y-%m-%dT02:00:00') \
    + '&ObjectId=D070FE3B29AFE6D9DF1D918616262AB1&Type=all&utilType=E&View=usage'

    s = requests.Session()
    response = s.post(url, data=post_data, headers=Headers, verify=False)
    c = s.cookies
    r = requests.get(p, cookies = c, verify = False)
    with open(os.path.join(os.getcwd(), fileName), 'wb') as fd:
        fd.write(r.content)

post_dict = {'username': os.environ['nbu_username'],'password':os.environ['nbu_password'],'saltkey':'SHA-256','kubraUserAuthentication':'false'}

Headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }

url_encoded_data = urlencode(post_dict)

post_data = url_encoded_data.encode("utf-8")

url = 'https://myinfo.nbutexas.com:443/CC/UserAuthentication'

#start = (datetime.today() + timedelta(days=-320)).replace(day=1)
start = datetime.today().replace(day=1)
end = (start + timedelta(days=32)).replace(day=1)

#for i in range(1, 3):
print("Start: " + start.strftime('%Y-%m-%dT00:00:00'))
print("End: " + end.strftime('%Y-%m-%dT00:00:00'))
print("\n")
getPowerUsage(start, end)
#end = start
#start = (start + timedelta(days=-3)).replace(day=1)




