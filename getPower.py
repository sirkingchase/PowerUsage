import os
import io
import ssl
import requests
from urllib.parse import urlencode
import pandas
from datetime import datetime, timedelta

def getPowerUsage(start, end):
    #generage headers for authenication
    post_dict = {'username': os.environ['nbu_username'],'password':os.environ['nbu_password'],'saltkey':'SHA-256','kubraUserAuthentication':'false'}
    Headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
    url_encoded_data = urlencode(post_dict)
    post_data = url_encoded_data.encode("utf-8")
    url = 'https://myinfo.nbutexas.com:443/CC/UserAuthentication'
    #authenticate and set cookie
    s = requests.Session()
    response = s.post(url, data=post_data, headers=Headers, verify=False)
    c = s.cookies
    #start.strftime('%Y-%m-%dT00:00:00') \
    #.strftime('%Y-%m-%dT02:00:00') \
    p='https://myinfo.nbutexas.com:443/CC/connect/users/home/indicators/ExportExcelReadData.xml' \
    + '&StartDateTime=' + start.strftime('%Y-%m-%dT00:00:00') \
    + '&EndDateTime=' + end.strftime('%Y-%m-%dT00:00:00') \
    + '&ObjectId=D070FE3B29AFE6D9DF1D918616262AB1&Type=all&utilType=E&View=usage'
    
    print(p)

    r = requests.get(p, cookies = c, verify = False)#download the CSV
    s = r.content
    powerRange = [i for i in range(0,26)]
    data = pandas.read_csv(io.StringIO(s.decode('utf-8')), usecols=powerRange)#read csv
    
    lastDate = data.iloc[-2,0]#get last date in csv file
    dt_object = datetime.strptime(lastDate, '%d %b %Y')#store as dt object
    fileName = "pu_" + start.strftime("%Y%m%d") + "-" + dt_object.strftime("%Y%m%d") + ".csv"
    with open(os.path.join(os.getcwd(), fileName), 'wb') as fd:
        fd.write(r.content)
    return fileName